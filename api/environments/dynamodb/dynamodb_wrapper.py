import logging
import typing
from contextlib import suppress
from typing import Any, Iterable

import boto3
from boto3.dynamodb.conditions import Key
from botocore.config import Config
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from flag_engine.environments.builders import build_environment_model
from flag_engine.identities.builders import build_identity_model
from flag_engine.identities.models import IdentityModel
from flag_engine.segments.evaluator import get_identity_segments
from rest_framework.exceptions import NotFound

if typing.TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import Table
    from mypy_boto3_dynamodb.type_defs import (
        QueryOutputTableTypeDef,
        TableAttributeValueTypeDef,
        QueryInputRequestTypeDef,
    )

from environments.dynamodb.constants import (
    DYNAMODB_MAX_BATCH_WRITE_ITEM_COUNT,
    ENVIRONMENTS_V2_PARTITION_KEY,
    ENVIRONMENTS_V2_SORT_KEY,
    IDENTITIES_PAGINATION_LIMIT,
)
from environments.dynamodb.types import IdentityOverridesV2Changeset
from environments.dynamodb.utils import (
    get_environments_v2_identity_override_document_key,
)
from util.mappers import (
    map_environment_api_key_to_environment_api_key_document,
    map_environment_to_environment_document,
    map_environment_to_environment_v2_document,
    map_identity_override_to_identity_override_document,
    map_identity_to_identity_document,
)
from util.util import iter_paired_chunks

if typing.TYPE_CHECKING:
    from environments.identities.models import Identity
    from environments.models import Environment, EnvironmentAPIKey

logger = logging.getLogger()


class BaseDynamoWrapper:
    table_name: str = None

    def __init__(self) -> None:
        self._table: typing.Optional["Table"] = None

    @property
    def table(self) -> typing.Optional["Table"]:
        if not self._table:
            self._table = self.get_table()
        return self._table

    def get_table_name(self) -> str:
        return self.table_name

    def get_table(self) -> typing.Optional["Table"]:
        if table_name := self.get_table_name():
            return boto3.resource("dynamodb", config=Config(tcp_keepalive=True)).Table(
                table_name
            )

    @property
    def is_enabled(self) -> bool:
        return self.table is not None


class DynamoIdentityWrapper(BaseDynamoWrapper):
    def get_table_name(self) -> str | None:
        return settings.IDENTITIES_TABLE_NAME_DYNAMO

    def query_items(self, *args, **kwargs) -> "QueryOutputTableTypeDef":
        return self.table.query(*args, **kwargs)

    def put_item(self, identity_dict: dict):
        self.table.put_item(Item=identity_dict)

    def write_identities(self, identities: Iterable["Identity"]):
        with self.table.batch_writer() as batch:
            for identity in identities:
                identity_document = map_identity_to_identity_document(identity)
                # Since sort keys can not be greater than 1024
                # https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#limits-partition-sort-keys
                if len(identity_document["identifier"]) > 1024:
                    logger.warning(
                        f"Can't migrate identity {identity.id}; identifier too long"
                    )
                    continue
                batch.put_item(Item=identity_document)

    def get_item(self, composite_key: str) -> typing.Optional[dict]:
        return self.table.get_item(Key={"composite_key": composite_key}).get("Item")

    def delete_item(self, composite_key: str):
        self.table.delete_item(Key={"composite_key": composite_key})

    def get_item_from_uuid(self, uuid: str) -> dict:
        filter_expression = Key("identity_uuid").eq(uuid)
        query_kwargs = {
            "IndexName": "identity_uuid-index",
            "Limit": 1,
            "KeyConditionExpression": filter_expression,
        }
        try:
            return self.query_items(**query_kwargs)["Items"][0]
        except IndexError:
            raise ObjectDoesNotExist()

    def get_item_from_uuid_or_404(self, uuid: str) -> dict:
        try:
            return self.get_item_from_uuid(uuid)
        except ObjectDoesNotExist as e:
            raise NotFound() from e

    def get_all_items(
        self,
        environment_api_key: str,
        limit: int,
        start_key: dict[str, "TableAttributeValueTypeDef"] | None = None,
    ) -> "QueryOutputTableTypeDef":
        filter_expression = Key("environment_api_key").eq(environment_api_key)
        query_kwargs: "QueryInputRequestTypeDef" = {
            "IndexName": "environment_api_key-identifier-index",
            "KeyConditionExpression": filter_expression,
            "Limit": limit,
        }
        if start_key:
            query_kwargs["ExclusiveStartKey"] = start_key
        return self.query_items(**query_kwargs)

    def iter_all_items_paginated(
        self,
        environment_api_key: str,
        limit: int = IDENTITIES_PAGINATION_LIMIT,
    ) -> typing.Generator[IdentityModel, None, None]:
        last_evaluated_key = "initial"
        get_all_items_kwargs = {
            "environment_api_key": environment_api_key,
            "limit": limit,
        }
        while last_evaluated_key:
            query_response = self.get_all_items(
                **get_all_items_kwargs,
            )
            for item in query_response["Items"]:
                yield IdentityModel.parse_obj(item)
            if last_evaluated_key := query_response.get("LastEvaluatedKey"):
                get_all_items_kwargs["start_key"] = last_evaluated_key

    def search_items_with_identifier(
        self,
        environment_api_key: str,
        identifier: str,
        search_function: typing.Callable,
        limit: int,
        start_key: dict = None,
    ):
        filter_expression = Key("environment_api_key").eq(
            environment_api_key
        ) & search_function(identifier)
        query_kwargs = {
            "IndexName": "environment_api_key-identifier-index",
            "Limit": limit,
            "KeyConditionExpression": filter_expression,
        }
        if start_key:
            query_kwargs.update(ExclusiveStartKey=start_key)
        return self.query_items(**query_kwargs)

    def get_segment_ids(
        self, identity_pk: str = None, identity_model: IdentityModel = None
    ) -> list:
        if not (identity_pk or identity_model):
            raise ValueError("Must provide one of identity_pk or identity_model.")

        with suppress(ObjectDoesNotExist):
            identity = identity_model or build_identity_model(
                self.get_item_from_uuid(identity_pk)
            )
            environment_wrapper = DynamoEnvironmentWrapper()
            environment = build_environment_model(
                environment_wrapper.get_item(identity.environment_api_key)
            )
            segments = get_identity_segments(environment, identity)
            return [segment.id for segment in segments]

        return []


class BaseDynamoEnvironmentWrapper(BaseDynamoWrapper):
    def write_environment(self, environment: "Environment") -> None:
        self.write_environments([environment])

    def write_environments(self, environments: Iterable["Environment"]) -> None:
        raise NotImplementedError()


class DynamoEnvironmentWrapper(BaseDynamoEnvironmentWrapper):
    table_name = settings.ENVIRONMENTS_TABLE_NAME_DYNAMO

    def write_environments(self, environments: Iterable["Environment"]):
        with self.table.batch_writer() as writer:
            for environment in environments:
                writer.put_item(
                    Item=map_environment_to_environment_document(environment),
                )

    def get_item(self, api_key: str) -> dict:
        try:
            return self.table.get_item(Key={"api_key": api_key})["Item"]
        except KeyError as e:
            raise ObjectDoesNotExist() from e


class DynamoEnvironmentV2Wrapper(BaseDynamoEnvironmentWrapper):
    def get_table_name(self) -> str | None:
        return settings.ENVIRONMENTS_V2_TABLE_NAME_DYNAMO

    def get_identity_overrides_by_environment_id(
        self,
        environment_id: int,
        feature_id: int | None = None,
    ) -> typing.List[dict[str, Any]]:
        try:
            response = self.table.query(
                KeyConditionExpression=Key(ENVIRONMENTS_V2_PARTITION_KEY).eq(
                    str(environment_id),
                )
                & Key(ENVIRONMENTS_V2_SORT_KEY).begins_with(
                    get_environments_v2_identity_override_document_key(
                        feature_id=feature_id,
                    ),
                )
            )
            return response["Items"]
        except KeyError as e:
            raise ObjectDoesNotExist() from e

    def update_identity_overrides(
        self,
        changeset: IdentityOverridesV2Changeset,
    ) -> None:
        for to_put, to_delete in iter_paired_chunks(
            changeset.to_put,
            changeset.to_delete,
            chunk_size=DYNAMODB_MAX_BATCH_WRITE_ITEM_COUNT,
        ):
            with self.table.batch_writer() as writer:
                for identity_override_to_delete in to_delete:
                    writer.delete_item(
                        Key={
                            ENVIRONMENTS_V2_PARTITION_KEY: identity_override_to_delete.environment_id,
                            ENVIRONMENTS_V2_SORT_KEY: identity_override_to_delete.document_key,
                        },
                    )
                for identity_override_to_put in to_put:
                    writer.put_item(
                        Item=map_identity_override_to_identity_override_document(
                            identity_override_to_put
                        ),
                    )

    def write_environments(self, environments: Iterable["Environment"]) -> None:
        with self.table.batch_writer() as writer:
            for environment in environments:
                writer.put_item(
                    Item=map_environment_to_environment_v2_document(environment),
                )


class DynamoEnvironmentAPIKeyWrapper(BaseDynamoWrapper):
    table_name = settings.ENVIRONMENTS_API_KEY_TABLE_NAME_DYNAMO

    def write_api_key(self, api_key: "EnvironmentAPIKey"):
        self.write_api_keys([api_key])

    def write_api_keys(self, api_keys: Iterable["EnvironmentAPIKey"]):
        with self.table.batch_writer() as writer:
            for api_key in api_keys:
                writer.put_item(
                    Item=map_environment_api_key_to_environment_api_key_document(
                        api_key
                    )
                )
