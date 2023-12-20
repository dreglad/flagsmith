# Changelog

## [2.91.0](https://github.com/Flagsmith/flagsmith/compare/v2.90.0...v2.91.0) (2023-12-20)


### Features

* add new url from role groups ([#3178](https://github.com/Flagsmith/flagsmith/issues/3178)) ([eebc541](https://github.com/Flagsmith/flagsmith/commit/eebc541e89daedfba4c98716d88c3ff5d4943032))


### Bug Fixes

* **admin/task-processor:** handle no task run ([#3196](https://github.com/Flagsmith/flagsmith/issues/3196)) ([eab1f6d](https://github.com/Flagsmith/flagsmith/commit/eab1f6db74a9b0ba728e081bcc6ce83001553b15))

## [2.90.0](https://github.com/Flagsmith/flagsmith/compare/v2.89.0...v2.90.0) (2023-12-20)


### Features

* **task-processor:** Add recurring task to clean password reset ([#3153](https://github.com/Flagsmith/flagsmith/issues/3153)) ([6898253](https://github.com/Flagsmith/flagsmith/commit/6898253d10e2347b9a309e81e0766761ce560e83))


### Bug Fixes

* **sse/tracking:** Use INFLUXDB_BUCKET for storing data ([#3197](https://github.com/Flagsmith/flagsmith/issues/3197)) ([fbd14fe](https://github.com/Flagsmith/flagsmith/commit/fbd14feed3aa2e3ffc861ce304e973f06614f91a))
* **task-processor/task-definition:** set RUN_BY_PROCESSOR ([#3195](https://github.com/Flagsmith/flagsmith/issues/3195)) ([f478def](https://github.com/Flagsmith/flagsmith/commit/f478def5af554752c0824d3fb7110d0052ad7406))
* **ui:** SAML should not be in Scale-up ([#3189](https://github.com/Flagsmith/flagsmith/issues/3189)) ([e6822bd](https://github.com/Flagsmith/flagsmith/commit/e6822bda01443c7fc05b5070ea90f490f0b4f6be))

## [2.89.0](https://github.com/Flagsmith/flagsmith/compare/v2.88.0...v2.89.0) (2023-12-19)


### Features

* Count v2 identity overrides for feature state list view ([#3164](https://github.com/Flagsmith/flagsmith/issues/3164)) ([65be52b](https://github.com/Flagsmith/flagsmith/commit/65be52b72835ba36075b499fdac59a1ace61b6ec))
* Create flagsmith on flagsmith feature export task ([#3149](https://github.com/Flagsmith/flagsmith/issues/3149)) ([e74ba0f](https://github.com/Flagsmith/flagsmith/commit/e74ba0f13ec17a3c949a9b3d1f68c2e15419d04e))
* Organisation reverts to free plan ([#3096](https://github.com/Flagsmith/flagsmith/issues/3096)) ([e5efdc8](https://github.com/Flagsmith/flagsmith/commit/e5efdc861cb6f88ac60dc503a596683f8a5ec0f1))
* **postgres/analytics:** Add task to clean-up old data ([#3170](https://github.com/Flagsmith/flagsmith/issues/3170)) ([8c8ce1f](https://github.com/Flagsmith/flagsmith/commit/8c8ce1f60478de197b95fc148abcaed680f2c5e5))
* Write migrated environments to v2 ([#3147](https://github.com/Flagsmith/flagsmith/issues/3147)) ([5914860](https://github.com/Flagsmith/flagsmith/commit/59148603b1566ef630d0b78118a540a210fb1624))


### Bug Fixes

* Add missing f-string from app_analytics models ([#3155](https://github.com/Flagsmith/flagsmith/issues/3155)) ([58d6589](https://github.com/Flagsmith/flagsmith/commit/58d6589889647a71fe22dacc4d960225996eee20))
* change request rendering issue when author no longer belongs to organisation ([#3087](https://github.com/Flagsmith/flagsmith/issues/3087)) ([8087fe2](https://github.com/Flagsmith/flagsmith/commit/8087fe2b65cd2ec2c945ea6d7d88332645f335ee))
* **Dockerfile:** setup gnupg correctly for nobody ([#3167](https://github.com/Flagsmith/flagsmith/issues/3167)) ([4759876](https://github.com/Flagsmith/flagsmith/commit/47598768d672dd1623abb822753317ddcc6c570c))
* Fine tune feature import export ([#3163](https://github.com/Flagsmith/flagsmith/issues/3163)) ([79e67ee](https://github.com/Flagsmith/flagsmith/commit/79e67ee40b06071093c580ab96649e2d5873407f))
* hide identity overrides badge or edge projects ([#3156](https://github.com/Flagsmith/flagsmith/issues/3156)) ([6a44b3d](https://github.com/Flagsmith/flagsmith/commit/6a44b3dd90cc9ff549dd99752618decd8d3cac9c))

## [2.88.0](https://github.com/Flagsmith/flagsmith/compare/v2.87.0...v2.88.0) (2023-12-13)


### Features

* Add a task for writing (edge) identity overrides ([#3127](https://github.com/Flagsmith/flagsmith/issues/3127)) ([2a9cd7c](https://github.com/Flagsmith/flagsmith/commit/2a9cd7cace471c2876f455436a9c5b0dd5cb4d45))
* add attribute to store identity overrides storage type ([#3109](https://github.com/Flagsmith/flagsmith/issues/3109)) ([c31322b](https://github.com/Flagsmith/flagsmith/commit/c31322bd4ed661d8ef23130cdcc0f4ad57a94153))
* Add dunning banner ([#3114](https://github.com/Flagsmith/flagsmith/issues/3114)) ([ad26100](https://github.com/Flagsmith/flagsmith/commit/ad261009de88ad12f831173dd192557278b4a7a9))
* add endpoint to list (edge) identity overrides for a feature ([#3116](https://github.com/Flagsmith/flagsmith/issues/3116)) ([098ab94](https://github.com/Flagsmith/flagsmith/commit/098ab94b17b5e7787252ec557dd3727e5bdd4342))
* Add new url for role users ([#3120](https://github.com/Flagsmith/flagsmith/issues/3120)) ([0604ec1](https://github.com/Flagsmith/flagsmith/commit/0604ec1467295887f608af379f081e4bf7ce04fc))
* Add Payment component in the blocked page ([#3068](https://github.com/Flagsmith/flagsmith/issues/3068)) ([3f100d2](https://github.com/Flagsmith/flagsmith/commit/3f100d20bee2d35342c9f8bc4294d0f68b84b3c9))
* explicitly set audit log created date ([#3083](https://github.com/Flagsmith/flagsmith/issues/3083)) ([e470ddb](https://github.com/Flagsmith/flagsmith/commit/e470ddb2f2fb7f4bf0fe4fe2afbe4744afff5ee3))
* Flag group owners ([#3112](https://github.com/Flagsmith/flagsmith/issues/3112)) ([b0a00d0](https://github.com/Flagsmith/flagsmith/commit/b0a00d0175460828038cb68656ea70d2a5fb3f0e))
* Import / export of features across environments and orgs ([#3026](https://github.com/Flagsmith/flagsmith/issues/3026)) ([c4bdc0f](https://github.com/Flagsmith/flagsmith/commit/c4bdc0fee57d2bb833e3b0f46dfb4b33f2c4acf8))
* Migrate given project's (edge) identities to environments v2 ([#3138](https://github.com/Flagsmith/flagsmith/issues/3138)) ([574a08e](https://github.com/Flagsmith/flagsmith/commit/574a08e274b1ee8de56faa765b3bb9a4ec464473))
* Set feature export response on initial API request ([#3126](https://github.com/Flagsmith/flagsmith/issues/3126)) ([89b7c8c](https://github.com/Flagsmith/flagsmith/commit/89b7c8c152a0e60c0816b56edc9339de645175f3))
* **sse:** track usage  ([#3050](https://github.com/Flagsmith/flagsmith/issues/3050)) ([9502e55](https://github.com/Flagsmith/flagsmith/commit/9502e55ea9c9fc67bfb4255e8485bff1ac018d2a))


### Bug Fixes

* **api-deploy/action.yml:** Write the PGP key correctly  ([#3099](https://github.com/Flagsmith/flagsmith/issues/3099)) ([c1c45cb](https://github.com/Flagsmith/flagsmith/commit/c1c45cbe1a8acc6feaa5182cc0f908626e0e51e6))
* bump rbac to fix import issue ([#3128](https://github.com/Flagsmith/flagsmith/issues/3128)) ([ba33582](https://github.com/Flagsmith/flagsmith/commit/ba33582863fe4d2e7cbe320ff8bd92a68ae6e8e5))
* do not show identity overrides tab until release ([#3134](https://github.com/Flagsmith/flagsmith/issues/3134)) ([b1fb768](https://github.com/Flagsmith/flagsmith/commit/b1fb768b29b7b9e9ef8dffa12e1a29613b08fc5c))
* **Dockerfile:** Use correct secret ID for pgp_key ([#3141](https://github.com/Flagsmith/flagsmith/issues/3141)) ([44ee410](https://github.com/Flagsmith/flagsmith/commit/44ee410b56ee3250bee27878bf3b4e79a885569a))
* Environments metadata n+1 for project admin ([#3101](https://github.com/Flagsmith/flagsmith/issues/3101)) ([093fa3a](https://github.com/Flagsmith/flagsmith/commit/093fa3a42f0f2c0d8e00c8a7ac9e4ef306f93831))
* hide additional actions on identity overrides tab in Edge ([#3135](https://github.com/Flagsmith/flagsmith/issues/3135)) ([5e0093e](https://github.com/Flagsmith/flagsmith/commit/5e0093ebebc9b4e2e3521353508dbe109c5087ec))
* Husky install ([#3137](https://github.com/Flagsmith/flagsmith/issues/3137)) ([921b210](https://github.com/Flagsmith/flagsmith/commit/921b2100b92581bf98cb1a28757fdac34a1f537b))
* Manage members layout is broken ([#3058](https://github.com/Flagsmith/flagsmith/issues/3058)) ([d129397](https://github.com/Flagsmith/flagsmith/commit/d129397a8ff91bcde022c3516582318bd2be6b94))
* re-add identity overrides for core projects ([#3139](https://github.com/Flagsmith/flagsmith/issues/3139)) ([8a5c20f](https://github.com/Flagsmith/flagsmith/commit/8a5c20f71038614e16e6b2e29c08931d82bf4c92))
* show falsy values in identity overrides ([#3144](https://github.com/Flagsmith/flagsmith/issues/3144)) ([68cfd15](https://github.com/Flagsmith/flagsmith/commit/68cfd156211e30e82aa16fb31cfc9864510037b6))
* Show scheduled change request ([#3118](https://github.com/Flagsmith/flagsmith/issues/3118)) ([efddf13](https://github.com/Flagsmith/flagsmith/commit/efddf13b5ed66818979eea60d63c3bcba64f7f94))
* **sse_recurring_task:** reload sse/tasks ([#3108](https://github.com/Flagsmith/flagsmith/issues/3108)) ([4e8e321](https://github.com/Flagsmith/flagsmith/commit/4e8e32156f527af72f4a9f806ca3b72a994e9dbf))
* **tests/NoCredentialsError:** use aws_credentials fixture ([#3131](https://github.com/Flagsmith/flagsmith/issues/3131)) ([7883e28](https://github.com/Flagsmith/flagsmith/commit/7883e283d403f8a518ac592e60642322968cb251))
* Unable to delete multiple segment overrides at once ([#3100](https://github.com/Flagsmith/flagsmith/issues/3100)) ([9e6e0ca](https://github.com/Flagsmith/flagsmith/commit/9e6e0ca91f750350b3dda4c98ac644436de9c51a))

## [2.87.0](https://github.com/Flagsmith/flagsmith/compare/v2.86.0...v2.87.0) (2023-12-05)


### Features

* add new endpoint to list summary objects of permission groups ([#3064](https://github.com/Flagsmith/flagsmith/issues/3064)) ([2880ef5](https://github.com/Flagsmith/flagsmith/commit/2880ef55cdf7eadfc50ef71217f57d20d7e83fff))


### Bug Fixes

* Add group owners to missing endpoint ([#3080](https://github.com/Flagsmith/flagsmith/issues/3080)) ([8fe2ea7](https://github.com/Flagsmith/flagsmith/commit/8fe2ea7a1ca9c069a0608c91d73660920414af22))
* Move environments and features to test area ([#3081](https://github.com/Flagsmith/flagsmith/issues/3081)) ([05a3b37](https://github.com/Flagsmith/flagsmith/commit/05a3b37319cbad8ba0ccae38c76b9db4e503b966))
* **postgres/feature-analytics:** use feature filter ([#3091](https://github.com/Flagsmith/flagsmith/issues/3091)) ([c0fc231](https://github.com/Flagsmith/flagsmith/commit/c0fc231a2c4d2c1b41e07aebd5721bd8a477a691))
* Reading role permissions generates 500 error backend ([#3079](https://github.com/Flagsmith/flagsmith/issues/3079)) ([cee607a](https://github.com/Flagsmith/flagsmith/commit/cee607a7ef19c0d0eed91ecf01ee44476214f440))
* Refactor existing Chargebee webhooks for subscriptions ([#3047](https://github.com/Flagsmith/flagsmith/issues/3047)) ([c89c56a](https://github.com/Flagsmith/flagsmith/commit/c89c56aaa694976e80e7b47d90b28921b0fdfece))
* remove pagination from group summaries ([#3090](https://github.com/Flagsmith/flagsmith/issues/3090)) ([1065ad0](https://github.com/Flagsmith/flagsmith/commit/1065ad0258c36e76cca6a106d4888ffdc329d54e))
* resolve outstanding N+1 issues ([#3066](https://github.com/Flagsmith/flagsmith/issues/3066)) ([661c42f](https://github.com/Flagsmith/flagsmith/commit/661c42f52c2c525d57a2c52954440b5444fd7fbf))
* revert "fix: Reading role permissions generates 500 error backend" ([#3093](https://github.com/Flagsmith/flagsmith/issues/3093)) ([e57a01c](https://github.com/Flagsmith/flagsmith/commit/e57a01cf54ce07a18b757b4c5e9707c247c89639))

## [2.86.0](https://github.com/Flagsmith/flagsmith/compare/v2.85.0...v2.86.0) (2023-11-30)


### Features

* **auth:** integrate ldap ([#3031](https://github.com/Flagsmith/flagsmith/issues/3031)) ([65f78f7](https://github.com/Flagsmith/flagsmith/commit/65f78f79c78fb272de1052ff1a2e6c830af50318))


### Bug Fixes

* only run index queries for Postgres DBs ([#3055](https://github.com/Flagsmith/flagsmith/issues/3055)) ([7664ea2](https://github.com/Flagsmith/flagsmith/commit/7664ea2073fcaed35f13a7ce6f4234d7b52fef2a))

## [2.85.0](https://github.com/Flagsmith/flagsmith/compare/v2.84.2...v2.85.0) (2023-11-28)


### Features

* Rebuild chargebee caches ([#3028](https://github.com/Flagsmith/flagsmith/issues/3028)) ([aed15c3](https://github.com/Flagsmith/flagsmith/commit/aed15c351d19813667de04245e9cb41560c15651))


### Bug Fixes

* Move projects and integrations to tests ([#3044](https://github.com/Flagsmith/flagsmith/issues/3044)) ([0dc4e14](https://github.com/Flagsmith/flagsmith/commit/0dc4e14aa10fa4f0401c2cac200e91a390700e28))
* Rely on Flagsmith Engine for segment evaluation, avoid N+1 queries ([#3038](https://github.com/Flagsmith/flagsmith/issues/3038)) ([616c6be](https://github.com/Flagsmith/flagsmith/commit/616c6be03a0b8c9dd742415c2fd2cde8cd08c95d))
* Safely parse announcement Flag ([#3052](https://github.com/Flagsmith/flagsmith/issues/3052)) ([6994f6b](https://github.com/Flagsmith/flagsmith/commit/6994f6bfb08eed104133fc13967ef68cac19b58b))

## [2.84.2](https://github.com/Flagsmith/flagsmith/compare/v2.84.1...v2.84.2) (2023-11-27)


### Bug Fixes

* Move organisation tests to proper location ([#3041](https://github.com/Flagsmith/flagsmith/issues/3041)) ([34c6d07](https://github.com/Flagsmith/flagsmith/commit/34c6d072adae2558c7fee4c58a61570a817fe23d))
* resolve environment N+1 caused by feature versioning v2 ([#3040](https://github.com/Flagsmith/flagsmith/issues/3040)) ([5392480](https://github.com/Flagsmith/flagsmith/commit/5392480c3e35fd689347a80714901d4f70116367))

## [2.84.1](https://github.com/Flagsmith/flagsmith/compare/v2.84.0...v2.84.1) (2023-11-27)


### Bug Fixes

* Revert to Core API segment evaluation ([#3036](https://github.com/Flagsmith/flagsmith/issues/3036)) ([e5058ae](https://github.com/Flagsmith/flagsmith/commit/e5058ae01cca1ceb783c38d2eb29c83f07a86a8c))

## [2.84.0](https://github.com/Flagsmith/flagsmith/compare/v2.83.0...v2.84.0) (2023-11-27)


### Features

* Feature Versioning V2 ([#2382](https://github.com/Flagsmith/flagsmith/issues/2382)) ([bcfb10e](https://github.com/Flagsmith/flagsmith/commit/bcfb10ece60d4c9ce751ceef8681a1d264d69291))
* Rely on Flagsmith Engine for segment evaluation ([#2865](https://github.com/Flagsmith/flagsmith/issues/2865)) ([322eb08](https://github.com/Flagsmith/flagsmith/commit/322eb08167a8cec4b052dabddd34b10e346dca9a))
* **ui:** hide API keys from integrations list ([#3019](https://github.com/Flagsmith/flagsmith/issues/3019)) ([b02a524](https://github.com/Flagsmith/flagsmith/commit/b02a524ad5932e1cb0ef447e3bb8aa754e966118))


### Bug Fixes

* WIP Move groups of tests to proper location ([#3027](https://github.com/Flagsmith/flagsmith/issues/3027)) ([1592919](https://github.com/Flagsmith/flagsmith/commit/159291919541b2c20e8302339b6a2e04722ce191))

## [2.83.0](https://github.com/Flagsmith/flagsmith/compare/v2.82.0...v2.83.0) (2023-11-21)


### Features

* introduce dunning billing status ([#2976](https://github.com/Flagsmith/flagsmith/issues/2976)) ([975c7b0](https://github.com/Flagsmith/flagsmith/commit/975c7b0d6438cd973ccd62b590436e4c2568b9d4))


### Bug Fixes

* **api:** validate before creating projects based on current subscription ([#2869](https://github.com/Flagsmith/flagsmith/issues/2869)) ([f32159e](https://github.com/Flagsmith/flagsmith/commit/f32159e3fd821c6dc7bfbd50a0c3d22374f1b558))
* **edge-identity-view:** reduce max page size to 100 ([#2937](https://github.com/Flagsmith/flagsmith/issues/2937)) ([6c4807f](https://github.com/Flagsmith/flagsmith/commit/6c4807f0b2dd2ee770d2d712b2955a9fd71c37a0))
* Move and merge features tests into proper location ([#3002](https://github.com/Flagsmith/flagsmith/issues/3002)) ([5f3482c](https://github.com/Flagsmith/flagsmith/commit/5f3482c8c376c6dd283ab4aff36dedb67825facc))

## [2.82.0](https://github.com/Flagsmith/flagsmith/compare/v2.81.1...v2.82.0) (2023-11-20)


### Features

* Add permission for manage segments overrides ([#2919](https://github.com/Flagsmith/flagsmith/issues/2919)) ([716f6a9](https://github.com/Flagsmith/flagsmith/commit/716f6a960a8843503e6af622eaea30a3924e9eb3))
* Add seats to next invoice ([#2977](https://github.com/Flagsmith/flagsmith/issues/2977)) ([e4325a8](https://github.com/Flagsmith/flagsmith/commit/e4325a872265d0c60415bac6545c8d040d31d00f))
* Remove all but first admin when subscription has reached cancellation date ([#2965](https://github.com/Flagsmith/flagsmith/issues/2965)) ([6976f81](https://github.com/Flagsmith/flagsmith/commit/6976f81c910d5d8de4f194fc27e799b72778b9f6))


### Bug Fixes

* add LDAP to installed apps ([#2993](https://github.com/Flagsmith/flagsmith/issues/2993)) ([9f9237e](https://github.com/Flagsmith/flagsmith/commit/9f9237ec8d9e017401316ded027989139e707bf2))
* ensure SimpleFeatureStateViewSet uses correct permissions for segment overrides ([#2990](https://github.com/Flagsmith/flagsmith/issues/2990)) ([00c6444](https://github.com/Flagsmith/flagsmith/commit/00c6444cc4abffb6bdd50e47f5f1e560667f8b85))
* Excessive 404s on subscription metadata ([#2985](https://github.com/Flagsmith/flagsmith/issues/2985)) ([627a6fa](https://github.com/Flagsmith/flagsmith/commit/627a6fa0b3d3609ac6e12aae7f9b71220f2567af))
* Failure to import LD project other than `default` ([#2979](https://github.com/Flagsmith/flagsmith/issues/2979)) ([e0d6e8a](https://github.com/Flagsmith/flagsmith/commit/e0d6e8acd9ef28d685fca724cef435bbefdbee3d))
* Logic in segment overrides readonly with the manage_segment_overrides permission ([#2973](https://github.com/Flagsmith/flagsmith/issues/2973)) ([37879b2](https://github.com/Flagsmith/flagsmith/commit/37879b2046cd7bcd1293ffa81c2bfcaff93798d3))
* Move tests to unit  ([#2987](https://github.com/Flagsmith/flagsmith/issues/2987)) ([43caad8](https://github.com/Flagsmith/flagsmith/commit/43caad803b4d04144099e9cdfb4554a1ef19cb14))
* opening the flag panel shifts the main table slightly ([#2994](https://github.com/Flagsmith/flagsmith/issues/2994)) ([85d980c](https://github.com/Flagsmith/flagsmith/commit/85d980c6cb817867848f4676744e4324df8f3f49))
* Pagination icons disappeared ([#2982](https://github.com/Flagsmith/flagsmith/issues/2982)) ([0d2b979](https://github.com/Flagsmith/flagsmith/commit/0d2b979354390e945bcd003e174c424ac7482f2e))
* Update docstring to not include change requests ([#2995](https://github.com/Flagsmith/flagsmith/issues/2995)) ([e3ac7ef](https://github.com/Flagsmith/flagsmith/commit/e3ac7ef063d81f4264b3a03552dd67925e31382b))
* Update endpoint getEnvironment RTK response ([#2968](https://github.com/Flagsmith/flagsmith/issues/2968)) ([3993823](https://github.com/Flagsmith/flagsmith/commit/39938239a6f58a0266c9a32f35ee6c5ae7c15c5c))

## [2.81.1](https://github.com/Flagsmith/flagsmith/compare/v2.81.0...v2.81.1) (2023-11-14)


### Bug Fixes

* try self-hosted runner for the private cloud image ([#2969](https://github.com/Flagsmith/flagsmith/issues/2969)) ([99180cd](https://github.com/Flagsmith/flagsmith/commit/99180cdbf3cc3362efbb80eb83d131d066ae0f5f))

## [2.81.0](https://github.com/Flagsmith/flagsmith/compare/v2.80.0...v2.81.0) (2023-11-14)


### Features

* add foundation for LDAP in core repository ([#2923](https://github.com/Flagsmith/flagsmith/issues/2923)) ([65351e2](https://github.com/Flagsmith/flagsmith/commit/65351e205e268e49b01567ab7ed06fbaa1107643))
* Add manage segment overrides permission in UI ([#2936](https://github.com/Flagsmith/flagsmith/issues/2936)) ([88c43cd](https://github.com/Flagsmith/flagsmith/commit/88c43cda72cb747735254de44ae0ed78bc954808))
* Allow organisation admins to mandate 2fa for their organisation ([#2877](https://github.com/Flagsmith/flagsmith/issues/2877)) ([1d006fb](https://github.com/Flagsmith/flagsmith/commit/1d006fbc1515e16582210554b562d4aec2b382d5))
* trial management in sales dashboard ([#2805](https://github.com/Flagsmith/flagsmith/issues/2805)) ([a056713](https://github.com/Flagsmith/flagsmith/commit/a056713c31b11302b9445a57929b6a4ee9e4d109))


### Bug Fixes

* Audit Log records don't get created with threaded task processing ([#2958](https://github.com/Flagsmith/flagsmith/issues/2958)) ([716b228](https://github.com/Flagsmith/flagsmith/commit/716b2281c1d15277cfd9f48843970fc3c785719d))
* Fix evironment metadata N+1 for environments list ([#2947](https://github.com/Flagsmith/flagsmith/issues/2947)) ([7e1c779](https://github.com/Flagsmith/flagsmith/commit/7e1c77911af7c9cdbbdb6f9b1dff6c7c95becc52))
* Handle payment errors during user flow ([#2951](https://github.com/Flagsmith/flagsmith/issues/2951)) ([b18e4a6](https://github.com/Flagsmith/flagsmith/commit/b18e4a6d6588e80be4575de1891d51f10040ebef))
* Move organisation tests ([#2964](https://github.com/Flagsmith/flagsmith/issues/2964)) ([01d14d2](https://github.com/Flagsmith/flagsmith/commit/01d14d2ce23c787bbcea417fefb97b85a56b6413))
* sales dashboard subscription metadata shows wrong data after starting trial ([#2962](https://github.com/Flagsmith/flagsmith/issues/2962)) ([9a49f7d](https://github.com/Flagsmith/flagsmith/commit/9a49f7dcac5c01741cc5625314215edb04f1a3ea))

## [2.80.0](https://github.com/Flagsmith/flagsmith/compare/v2.79.0...v2.80.0) (2023-11-13)


### Features

* add copy button to server keys ([#2943](https://github.com/Flagsmith/flagsmith/issues/2943)) ([b78842b](https://github.com/Flagsmith/flagsmith/commit/b78842b6041cff8edc8c8091f79b47953568a63d))
* Add or remove user and groups from roles ([#2791](https://github.com/Flagsmith/flagsmith/issues/2791)) ([c2d0c11](https://github.com/Flagsmith/flagsmith/commit/c2d0c1142f5beb18c90c14e35c3eb329aafc26b4))
* **boto3/dynamo:** use tcp_keepalive ([#2926](https://github.com/Flagsmith/flagsmith/issues/2926)) ([eee1c0a](https://github.com/Flagsmith/flagsmith/commit/eee1c0a647331dd49ebd81fbc9cc0e1b53ce6c72))


### Bug Fixes

* Check that feature owners are able to view the project of a feature ([#2931](https://github.com/Flagsmith/flagsmith/issues/2931)) ([a0eefdd](https://github.com/Flagsmith/flagsmith/commit/a0eefdd3223cb0e684eb4aed36f21b9ea4f9d370))
* Close icon missing in roles modal ([#2946](https://github.com/Flagsmith/flagsmith/issues/2946)) ([4960f7e](https://github.com/Flagsmith/flagsmith/commit/4960f7e51f63b6483a5751dc435a67e20bcb6499))
* creating change requests in private cloud UI ([#2953](https://github.com/Flagsmith/flagsmith/issues/2953)) ([8eedf55](https://github.com/Flagsmith/flagsmith/commit/8eedf55ab34a9eedeea9c11e1dd9ac7b8e0ffa61))
* **deps:** CVE dependency updates (PVE-2023-61661, PVE-2023-61657, PV… ([#2939](https://github.com/Flagsmith/flagsmith/issues/2939)) ([ac26fc9](https://github.com/Flagsmith/flagsmith/commit/ac26fc97fb9aa461357973a25ab52741ccbfc7d9))
* Infinite loop 404 after leaving the organisation ([#2957](https://github.com/Flagsmith/flagsmith/issues/2957)) ([7b7f986](https://github.com/Flagsmith/flagsmith/commit/7b7f9860e63806552353f092d3d61a9d23f8c0af))
* prevent sentry errors for on premise subscriptions ([#2948](https://github.com/Flagsmith/flagsmith/issues/2948)) ([6f830e2](https://github.com/Flagsmith/flagsmith/commit/6f830e2b2124dd50d2cd078e156d028c5b9f9ae9))
* Rebuild environments when stop serving flags changed ([#2944](https://github.com/Flagsmith/flagsmith/issues/2944)) ([7d16197](https://github.com/Flagsmith/flagsmith/commit/7d161972e9a9e7ffbffbff905ae0053d86bd35f9))

## [2.79.0](https://github.com/Flagsmith/flagsmith/compare/v2.78.0...v2.79.0) (2023-11-07)


### Features

* add group owners to features ([#2908](https://github.com/Flagsmith/flagsmith/issues/2908)) ([493f0e5](https://github.com/Flagsmith/flagsmith/commit/493f0e5a09bb92dab38e13419e7b5c320e9779dd))
* Create staff fixture ([#2928](https://github.com/Flagsmith/flagsmith/issues/2928)) ([a09436d](https://github.com/Flagsmith/flagsmith/commit/a09436ddde7fd7c68a8e75b1dd311d5ac804f397))


### Bug Fixes

* Tighten ACL for user routes ([#2929](https://github.com/Flagsmith/flagsmith/issues/2929)) ([3732e67](https://github.com/Flagsmith/flagsmith/commit/3732e67f2dc1c0010ad5d4796960af2ddedf90c9))

## [2.78.0](https://github.com/Flagsmith/flagsmith/compare/v2.77.0...v2.78.0) (2023-11-01)


### Features

* **task-processor:** Add priority support  ([#2847](https://github.com/Flagsmith/flagsmith/issues/2847)) ([6830ef6](https://github.com/Flagsmith/flagsmith/commit/6830ef666c7f9931a4d4edfeef9e58e7d2768dcc))


### Bug Fixes

* Revert "ci: Run only API tests affected by changes in PRs and Upgrade GHA runners" ([#2910](https://github.com/Flagsmith/flagsmith/issues/2910)) ([6a730c7](https://github.com/Flagsmith/flagsmith/commit/6a730c7ae87b06df13af82b4c51dd113343c6333))
* **task/priority:** change field to SmallIntegerField ([#2914](https://github.com/Flagsmith/flagsmith/issues/2914)) ([6e6a48b](https://github.com/Flagsmith/flagsmith/commit/6e6a48be303197ebc90d096b44c4b75d7a22c778))

## [2.77.0](https://github.com/Flagsmith/flagsmith/compare/v2.76.0...v2.77.0) (2023-10-30)


### Features

* Click Segment Overrides icon doesnt open the segment override tab ([#2887](https://github.com/Flagsmith/flagsmith/issues/2887)) ([96f3b22](https://github.com/Flagsmith/flagsmith/commit/96f3b22f3d21d81074643df90878dba2ace51580))
* **permissions/tags:** Add tags support  ([#2685](https://github.com/Flagsmith/flagsmith/issues/2685)) ([78e559c](https://github.com/Flagsmith/flagsmith/commit/78e559c320011bcc6ec9339cb2614a9751244156))


### Bug Fixes

* Handle null tooltip data ([#2892](https://github.com/Flagsmith/flagsmith/issues/2892)) ([a1190ae](https://github.com/Flagsmith/flagsmith/commit/a1190ae90a31496e9e368a1dbdc232a1dd4daf1a))

## [2.76.0](https://github.com/Flagsmith/flagsmith/compare/v2.75.0...v2.76.0) (2023-10-24)


### Features

* **rate-limit:** allow user to pass default throttle classes ([#2878](https://github.com/Flagsmith/flagsmith/issues/2878)) ([dc4b02c](https://github.com/Flagsmith/flagsmith/commit/dc4b02c7c3a67c34f16146c686786ffb09367ecf))

## [2.75.0](https://github.com/Flagsmith/flagsmith/compare/v2.74.0...v2.75.0) (2023-10-23)


### Features

* partial imports, off values as control value ([#2864](https://github.com/Flagsmith/flagsmith/issues/2864)) ([93df958](https://github.com/Flagsmith/flagsmith/commit/93df958b8fc67d17c6cfc298184bfef0f83847b4))
* update change request layout ([#2848](https://github.com/Flagsmith/flagsmith/issues/2848)) ([eaffffe](https://github.com/Flagsmith/flagsmith/commit/eaffffe0d0313eaadbf25980ea42afeb1e753ffd))


### Bug Fixes

* Cannot see the assigned users in the changes request section ([#2868](https://github.com/Flagsmith/flagsmith/issues/2868)) ([59abf20](https://github.com/Flagsmith/flagsmith/commit/59abf20f59b92c5f47d7ddfc698c81eb695e3bb4))
* rate limit admin endpoints ([#2703](https://github.com/Flagsmith/flagsmith/issues/2703)) ([b0ef013](https://github.com/Flagsmith/flagsmith/commit/b0ef0134cf40703de225ffa3ad4363fee4f8f997))

## [2.74.0](https://github.com/Flagsmith/flagsmith/compare/v2.73.1...v2.74.0) (2023-10-18)


### Features

* Launchdarkly importer ([#2530](https://github.com/Flagsmith/flagsmith/issues/2530)) ([4f7464b](https://github.com/Flagsmith/flagsmith/commit/4f7464b24aba4f0cf0fb79379dbde1275f50f71a))
* LaunchDarkly importer UI ([#2837](https://github.com/Flagsmith/flagsmith/issues/2837)) ([a78eeaf](https://github.com/Flagsmith/flagsmith/commit/a78eeaf4cae8b84ef3b45f5edd761dc46da966ba))


### Bug Fixes

* enable audit for import events ([#2849](https://github.com/Flagsmith/flagsmith/issues/2849)) ([7964e49](https://github.com/Flagsmith/flagsmith/commit/7964e4999cbea031422aa610282cbacc303d8177))
* incorrect default_percentage_allocation on import, binary flags imported as multivariate ([#2841](https://github.com/Flagsmith/flagsmith/issues/2841)) ([619c3f5](https://github.com/Flagsmith/flagsmith/commit/619c3f52a821d8eaace2035c5e34b51b16040deb))
* Logged out of Flagsmith when testing Webhook ([#2842](https://github.com/Flagsmith/flagsmith/issues/2842)) ([cfbf7f1](https://github.com/Flagsmith/flagsmith/commit/cfbf7f192e699c9318c97a05266e31ff7d680e3d))

## [2.73.1](https://github.com/Flagsmith/flagsmith/compare/v2.73.0...v2.73.1) (2023-10-05)


### Bug Fixes

* **tasks:** Create a different task to update environment document  ([#2807](https://github.com/Flagsmith/flagsmith/issues/2807)) ([ab21983](https://github.com/Flagsmith/flagsmith/commit/ab21983e8736d4244df2cd37c235d8ce4795e948))

## [2.73.0](https://github.com/Flagsmith/flagsmith/compare/v2.72.1...v2.73.0) (2023-10-05)


### Features

* **tasks/queue-size:** Implement queue_size ([#2826](https://github.com/Flagsmith/flagsmith/issues/2826)) ([94fff2c](https://github.com/Flagsmith/flagsmith/commit/94fff2c53bc80ada60c18bf5bfd91c700d363d61))


### Bug Fixes

* Project Dropdown selector is not sorted alphabetically ([#2812](https://github.com/Flagsmith/flagsmith/issues/2812)) ([7123cf6](https://github.com/Flagsmith/flagsmith/commit/7123cf67df7169576eaeb609f1d67b48097310bf))
* Shows "Identities" nav element as disabled for users without relevant permission ([#2813](https://github.com/Flagsmith/flagsmith/issues/2813)) ([3ec2f6b](https://github.com/Flagsmith/flagsmith/commit/3ec2f6b4d10019c757f336f23048342aab835d13))

## [2.72.1](https://github.com/Flagsmith/flagsmith/compare/v2.72.0...v2.72.1) (2023-09-28)


### Bug Fixes

* Last Influx data updated at never updates ([#2802](https://github.com/Flagsmith/flagsmith/issues/2802)) ([929afeb](https://github.com/Flagsmith/flagsmith/commit/929afeb49466bf0be893a2f5033c0fff8a6f8a1a))
* Payment modal ([#2792](https://github.com/Flagsmith/flagsmith/issues/2792)) ([c231749](https://github.com/Flagsmith/flagsmith/commit/c231749272d52d7b1a987aa2fdd82855e05f6d07))
* Price is missing in dark mode ([#2799](https://github.com/Flagsmith/flagsmith/issues/2799)) ([31c9884](https://github.com/Flagsmith/flagsmith/commit/31c9884b9cd3a518b14cf8b796c934c4303738a9))
* **seat-upgrades:** Allow auto seat upgrades for new scaleup plan ([#2809](https://github.com/Flagsmith/flagsmith/issues/2809)) ([1cada3c](https://github.com/Flagsmith/flagsmith/commit/1cada3ced81e9b9b4a4257a49ec0a9da9e305f1c))
* Toast messages look wrong ([#2800](https://github.com/Flagsmith/flagsmith/issues/2800)) ([f003732](https://github.com/Flagsmith/flagsmith/commit/f003732d89d4e2ad01a222083dcd68760faa6950))

## [2.72.0](https://github.com/Flagsmith/flagsmith/compare/v2.71.0...v2.72.0) (2023-09-19)


### Features

* Add a pill for server side only flags ([#2780](https://github.com/Flagsmith/flagsmith/issues/2780)) ([2b70c68](https://github.com/Flagsmith/flagsmith/commit/2b70c68d548a1f9a5ae30372506e503611d7c707))
* display warning and prevent creation on limit ([#2526](https://github.com/Flagsmith/flagsmith/issues/2526)) ([000be2b](https://github.com/Flagsmith/flagsmith/commit/000be2b0c071d6ef839da5d0febcc85b58e47ab7))
* Realtime updates, defaultFlags, cacheControl and timeout config for Android ([#2757](https://github.com/Flagsmith/flagsmith/issues/2757)) ([54de331](https://github.com/Flagsmith/flagsmith/commit/54de331af199a898e7850eeac30aeb9ac41a4d58))


### Bug Fixes

* Environment webhook update button not working ([#2788](https://github.com/Flagsmith/flagsmith/issues/2788)) ([5f92a00](https://github.com/Flagsmith/flagsmith/commit/5f92a0067034ae1ee95d3b3bb8c360eddd8996bb))
* Feature id in mv-option request is undefined ([#2751](https://github.com/Flagsmith/flagsmith/issues/2751)) ([3c3b1d7](https://github.com/Flagsmith/flagsmith/commit/3c3b1d7af2e4b62f75979b8c8c2ea931f8736cbd))
* fix segments display crashing ([#2770](https://github.com/Flagsmith/flagsmith/issues/2770)) ([#2789](https://github.com/Flagsmith/flagsmith/issues/2789)) ([bb080d2](https://github.com/Flagsmith/flagsmith/commit/bb080d2e11ecb6197406b483c58e694f66c95194))
* Send JSON response instead of plain text ([#2739](https://github.com/Flagsmith/flagsmith/issues/2739)) ([cad0cbf](https://github.com/Flagsmith/flagsmith/commit/cad0cbfb08fd34c2732ff5fefc2f5a5752cb60cf))

## [2.71.0](https://github.com/Flagsmith/flagsmith/compare/v2.70.2...v2.71.0) (2023-09-11)


### Features

* Add feature description like the old UI ([#2733](https://github.com/Flagsmith/flagsmith/issues/2733)) ([33e7c17](https://github.com/Flagsmith/flagsmith/commit/33e7c17b3f7b1cb7964c2f00ae8001faf251945e))
* **task-processor:** validate arguments passed to task processor functions ([#2747](https://github.com/Flagsmith/flagsmith/issues/2747)) ([d947474](https://github.com/Flagsmith/flagsmith/commit/d947474696a3a213ff196ffc5ac3bf802dbd8062))


### Bug Fixes

* allow registration via invite link if ALLOW_REGISTRATION_WITHOUT_INVITE is False ([#2731](https://github.com/Flagsmith/flagsmith/issues/2731)) ([73705d5](https://github.com/Flagsmith/flagsmith/commit/73705d57068ef63eb5c36b104dc25b68fa14dcfd))
* Deleting a project causes multiple UI issues ([#2749](https://github.com/Flagsmith/flagsmith/issues/2749)) ([8cd144b](https://github.com/Flagsmith/flagsmith/commit/8cd144b66069fbc0bdc934d67d44f9d4fd5d6d16))
* **featurestate-permissions:** Add misc extra checks ([#2712](https://github.com/Flagsmith/flagsmith/issues/2712)) ([ecb7fd2](https://github.com/Flagsmith/flagsmith/commit/ecb7fd2c0e352058609b07ac049d90ca9d2a36e5))
* UI issue when there were more than 100 features ([#2711](https://github.com/Flagsmith/flagsmith/issues/2711)) ([c1a62ce](https://github.com/Flagsmith/flagsmith/commit/c1a62ce47c57a30bdeeee2adb023e36bbf9ff579))
* update ecs staging docker ([#2759](https://github.com/Flagsmith/flagsmith/issues/2759)) ([34f9a5b](https://github.com/Flagsmith/flagsmith/commit/34f9a5b8b0b02dce76cf7d7488e76e2ce78ed279))
* Update Webhook button not working ([#2753](https://github.com/Flagsmith/flagsmith/issues/2753)) ([8566fe0](https://github.com/Flagsmith/flagsmith/commit/8566fe02c39a7ddd958f42ffcb59320948b72e38))
* Webhook doesnt show the environment selected ([#2748](https://github.com/Flagsmith/flagsmith/issues/2748)) ([79b6030](https://github.com/Flagsmith/flagsmith/commit/79b60307ea279a6a6ddc0324b9cf436e5a62ae23))

## [2.70.2](https://github.com/Flagsmith/flagsmith/compare/v2.70.1...v2.70.2) (2023-09-05)


### Bug Fixes

* **chargebee:** ensure multiple addons are counted to subscription limits ([#2741](https://github.com/Flagsmith/flagsmith/issues/2741)) ([2ac23a8](https://github.com/Flagsmith/flagsmith/commit/2ac23a8d4cc966dc66ab8d31da7c536aec355bd1))
* **migrations:** remove features/0060 set environment not null ([#2738](https://github.com/Flagsmith/flagsmith/issues/2738)) ([3aed121](https://github.com/Flagsmith/flagsmith/commit/3aed12170ce72bfd8ebca5a74153ca0b7dcec40c))

## [2.70.1](https://github.com/Flagsmith/flagsmith/compare/v2.70.0...v2.70.1) (2023-09-05)


### Bug Fixes

* remove migration health check ([#2736](https://github.com/Flagsmith/flagsmith/issues/2736)) ([e5483cb](https://github.com/Flagsmith/flagsmith/commit/e5483cbdcd6a79b278d41775e18a2722bd177a9d))

## [2.70.0](https://github.com/Flagsmith/flagsmith/compare/v2.69.1...v2.70.0) (2023-09-05)


### Features

* integrate flagsmith client into API layer ([#2447](https://github.com/Flagsmith/flagsmith/issues/2447)) ([e71efbb](https://github.com/Flagsmith/flagsmith/commit/e71efbb19d7e81b4601f5e50968a1ea362b6e32d))


### Bug Fixes

* **model/featurestate:** make environment not null ([#2708](https://github.com/Flagsmith/flagsmith/issues/2708)) ([55a9ef7](https://github.com/Flagsmith/flagsmith/commit/55a9ef7bcfc62b9752a7407fbfe545b2df6bb72c))

## [2.69.1](https://github.com/Flagsmith/flagsmith/compare/v2.69.0...v2.69.1) (2023-09-01)


### Bug Fixes

* Announcement desing ([#2721](https://github.com/Flagsmith/flagsmith/issues/2721)) ([45844d2](https://github.com/Flagsmith/flagsmith/commit/45844d2105534a6fe7819f4817de59816ca486dd))
* Button to go to the link doesnt close the announcement ([#2724](https://github.com/Flagsmith/flagsmith/issues/2724)) ([b7c92df](https://github.com/Flagsmith/flagsmith/commit/b7c92df09f02bdcbeab7a7b0b9c5f1491b1d5dff))
* make `OrganisationSubscriptionInformationCache.allowed_projects` nullable ([#2716](https://github.com/Flagsmith/flagsmith/issues/2716)) ([1b37c99](https://github.com/Flagsmith/flagsmith/commit/1b37c99d93471def56a5042afb78e15cc2d7727e))
* prevent error when addons is null ([#2722](https://github.com/Flagsmith/flagsmith/issues/2722)) ([003d782](https://github.com/Flagsmith/flagsmith/commit/003d7824acf5d3242d79664dde7ff51f9b2a1ac6))

## [2.69.0](https://github.com/Flagsmith/flagsmith/compare/v2.68.0...v2.69.0) (2023-08-31)


### Features

* Home page announcement ([#2710](https://github.com/Flagsmith/flagsmith/issues/2710)) ([9de235b](https://github.com/Flagsmith/flagsmith/commit/9de235b6cc68f6b467c7ccc7db3317b069c6dbd6))
* **master-api-key/roles:** Add roles to master api key ([#2436](https://github.com/Flagsmith/flagsmith/issues/2436)) ([a46295b](https://github.com/Flagsmith/flagsmith/commit/a46295b885ecaf2a40a2f626a46c3a46a323f833))
* Use get-metadata-subscription to get max_api_calls ([#2279](https://github.com/Flagsmith/flagsmith/issues/2279)) ([42049fc](https://github.com/Flagsmith/flagsmith/commit/42049fcca8372dc32b4dab0fb350b9d8dc15ab34))


### Bug Fixes

* ensure feature segments are cloned correctly ([#2706](https://github.com/Flagsmith/flagsmith/issues/2706)) ([414e62f](https://github.com/Flagsmith/flagsmith/commit/414e62f6821efb9bf85dfc72a1f76625c6e96b20))
* **env-clone/permission:** allow clone using CREATE_ENVIRONMENT ([#2675](https://github.com/Flagsmith/flagsmith/issues/2675)) ([edc3afc](https://github.com/Flagsmith/flagsmith/commit/edc3afcb84b624aedbc9af56861cc1eb0f60dcf3))
* environment document totals ([#2671](https://github.com/Flagsmith/flagsmith/issues/2671)) ([33c9bf2](https://github.com/Flagsmith/flagsmith/commit/33c9bf22dce4ff50e0e01a9c1351b31aee41411d))
* settings page margin ([#2707](https://github.com/Flagsmith/flagsmith/issues/2707)) ([ef0ca42](https://github.com/Flagsmith/flagsmith/commit/ef0ca42bad1c58d4ab7730bbf021c4ace3357315))

## [2.68.0](https://github.com/Flagsmith/flagsmith/compare/v2.67.0...v2.68.0) (2023-08-22)


### Features

* admin action to delete all segments for project ([#2646](https://github.com/Flagsmith/flagsmith/issues/2646)) ([4df1b80](https://github.com/Flagsmith/flagsmith/commit/4df1b8037796b1304ce2dc4353c51bc7a67b1178))
* re-add totals and limits ([#2631](https://github.com/Flagsmith/flagsmith/issues/2631)) ([7a6a2c8](https://github.com/Flagsmith/flagsmith/commit/7a6a2c8f929bc079526a852494e3cfb87f796fb3))


### Bug Fixes

* **frontend:** Disabled loading indicator when getting featuers so screen doesn't flicker ([#2598](https://github.com/Flagsmith/flagsmith/issues/2598)) ([830e899](https://github.com/Flagsmith/flagsmith/commit/830e8991e7526a0e05cbbcef22110189d4a8ba55))
* **password-reset:** rate limit password reset emails ([#2619](https://github.com/Flagsmith/flagsmith/issues/2619)) ([db98743](https://github.com/Flagsmith/flagsmith/commit/db98743d426c0ded932d5a624cf8bd00cf2c6a86))
* total api calls handling ([#2583](https://github.com/Flagsmith/flagsmith/issues/2583)) ([ff0da20](https://github.com/Flagsmith/flagsmith/commit/ff0da20c57c4d37829e6d32e60db35886529fc86))
* **user-create:** duplicate email error message ([#2642](https://github.com/Flagsmith/flagsmith/issues/2642)) ([7b65a8d](https://github.com/Flagsmith/flagsmith/commit/7b65a8d7d7b0a2d6b938170a67ba6cabc32d00df))

## [2.67.0](https://github.com/Flagsmith/flagsmith/compare/v2.66.2...v2.67.0) (2023-08-15)


### Features

* Compare identities ([#2616](https://github.com/Flagsmith/flagsmith/issues/2616)) ([aafce13](https://github.com/Flagsmith/flagsmith/commit/aafce134fd2d078fe244e6ed983e2f05cfff820b))


### Bug Fixes

* update POETRY_OPTS in private cloud build ([#2624](https://github.com/Flagsmith/flagsmith/issues/2624)) ([d76f84c](https://github.com/Flagsmith/flagsmith/commit/d76f84c202641011443831f5edd912bec01cd64f))

## [2.66.2](https://github.com/Flagsmith/flagsmith/compare/v2.66.1...v2.66.2) (2023-08-10)


### Bug Fixes

* revert totals attributes ([#2625](https://github.com/Flagsmith/flagsmith/issues/2625)) ([3905527](https://github.com/Flagsmith/flagsmith/commit/39055275d18023702b9906991ad418cb2857088f))

## [2.66.1](https://github.com/Flagsmith/flagsmith/compare/v2.66.0...v2.66.1) (2023-08-10)


### Bug Fixes

* issue retrieving project with master api key ([#2623](https://github.com/Flagsmith/flagsmith/issues/2623)) ([1514bf7](https://github.com/Flagsmith/flagsmith/commit/1514bf735d670de67b847873061797608387f039))
* update auth controller vars in private cloud image build ([#2620](https://github.com/Flagsmith/flagsmith/issues/2620)) ([863c863](https://github.com/Flagsmith/flagsmith/commit/863c863ef6b595c24f8cf1de95a851f9de6b2f0a))

## [2.66.0](https://github.com/Flagsmith/flagsmith/compare/v2.65.0...v2.66.0) (2023-08-10)


### Features

* add limits and totals to API responses ([#2615](https://github.com/Flagsmith/flagsmith/issues/2615)) ([321d435](https://github.com/Flagsmith/flagsmith/commit/321d43537a049bd8b8efecad1619e7b32aa0bf33))
* Migrate to poetry ([#2214](https://github.com/Flagsmith/flagsmith/issues/2214)) ([0754071](https://github.com/Flagsmith/flagsmith/commit/0754071edebaca400c0fb2db1169de0495a2c33b))


### Bug Fixes

* Associated segment overrides ([#2582](https://github.com/Flagsmith/flagsmith/issues/2582)) ([707d394](https://github.com/Flagsmith/flagsmith/commit/707d3949a93e2041b3b25ee71a3f1693a311772f))
* metadata validation causes AttributeError for patch requests ([#2614](https://github.com/Flagsmith/flagsmith/issues/2614)) ([5e13707](https://github.com/Flagsmith/flagsmith/commit/5e13707b911a53924496a2e57e72b436b4dec510))
* variation value overflow ([#2612](https://github.com/Flagsmith/flagsmith/issues/2612)) ([863161b](https://github.com/Flagsmith/flagsmith/commit/863161b60b31db9defb751da852d9835e20f6746))

## [2.65.0](https://github.com/Flagsmith/flagsmith/compare/v2.64.1...v2.65.0) (2023-08-04)


### Features

* Use isEnterprise from endpoint version response to determine permissions ([#2422](https://github.com/Flagsmith/flagsmith/issues/2422)) ([edf38ac](https://github.com/Flagsmith/flagsmith/commit/edf38ac8114a7148991ee47b216fa67a5ffd5e95))


### Bug Fixes

* ensure that migrate command exits with non zero error code ([#2578](https://github.com/Flagsmith/flagsmith/issues/2578)) ([6c96ccf](https://github.com/Flagsmith/flagsmith/commit/6c96ccfbb70e559b3b525e683563217f85fd406d))

## [2.64.1](https://github.com/Flagsmith/flagsmith/compare/v2.64.0...v2.64.1) (2023-08-03)


### Bug Fixes

* environment webhooks shows current date, not created date ([#2555](https://github.com/Flagsmith/flagsmith/issues/2555)) ([94fb957](https://github.com/Flagsmith/flagsmith/commit/94fb957e2beafaa2e303e63d0e9fc954e37daf85))
* Highlight encoding ([#2558](https://github.com/Flagsmith/flagsmith/issues/2558)) ([717f175](https://github.com/Flagsmith/flagsmith/commit/717f17579eb08d403439b51b932692eb8a118b90))
* Sanitize HTML tooltips ([#2538](https://github.com/Flagsmith/flagsmith/issues/2538)) ([f68ea54](https://github.com/Flagsmith/flagsmith/commit/f68ea5426a0fe704276725b29c5d1b4fad9aeb35))

## [2.64.0](https://github.com/Flagsmith/flagsmith/compare/v2.63.3...v2.64.0) (2023-07-31)


### Features

* **integrations:** add support for Amplitude base url ([#2534](https://github.com/Flagsmith/flagsmith/issues/2534)) ([5d52564](https://github.com/Flagsmith/flagsmith/commit/5d5256483dd99d05ceaf4cb08ea66191b1cbc852))

## [2.63.3](https://github.com/Flagsmith/flagsmith/compare/v2.63.2...v2.63.3) (2023-07-28)


### Bug Fixes

* allow creating integration configurations where deleted versions exist ([#2531](https://github.com/Flagsmith/flagsmith/issues/2531)) ([3430829](https://github.com/Flagsmith/flagsmith/commit/34308293a2b3a5dfa8f4b764e847e6cd297279ed))
* change request audit logs ([#2527](https://github.com/Flagsmith/flagsmith/issues/2527)) ([d7c459e](https://github.com/Flagsmith/flagsmith/commit/d7c459ed4f43b57d61259692a1efb5363a4f4d41))
* percentage allocation display ([#2518](https://github.com/Flagsmith/flagsmith/issues/2518)) ([f8b1d50](https://github.com/Flagsmith/flagsmith/commit/f8b1d50a62ec08bb1df8b00b9ba1edcc1b91aeb5))
* **roles/org-permission:** Add missing viewset ([#2495](https://github.com/Flagsmith/flagsmith/issues/2495)) ([2b56c7c](https://github.com/Flagsmith/flagsmith/commit/2b56c7cc52631686f8b28e9cdb03c7203ec6abdb))
* **SwaggerGenerationError:** Remove filterset_field ([#2539](https://github.com/Flagsmith/flagsmith/issues/2539)) ([6dba7bd](https://github.com/Flagsmith/flagsmith/commit/6dba7bdd0563a4916d9185555512d21e6d77643c))
* **tests:** support any webhook order ([#2524](https://github.com/Flagsmith/flagsmith/issues/2524)) ([da2b4a7](https://github.com/Flagsmith/flagsmith/commit/da2b4a7128a7b40605eed04774a703839777a841))

## [2.63.2](https://github.com/Flagsmith/flagsmith/compare/v2.63.1...v2.63.2) (2023-07-25)


### Bug Fixes

* ensure recurring tasks are unlocked after being picked up (but not executed) ([#2508](https://github.com/Flagsmith/flagsmith/issues/2508)) ([24c21ea](https://github.com/Flagsmith/flagsmith/commit/24c21ead348f5c3dc190468309459611336c4856))
* rendering recurring task admin times out ([#2514](https://github.com/Flagsmith/flagsmith/issues/2514)) ([cb95a92](https://github.com/Flagsmith/flagsmith/commit/cb95a925cc8907a8f37f76f48a840261c467372d))
* Update Hyperlink "Learn about Audit Webhooks" URL ([#2504](https://github.com/Flagsmith/flagsmith/issues/2504)) ([9ec20b5](https://github.com/Flagsmith/flagsmith/commit/9ec20b5214b95a9bfe481ac42511d1ff8fa1b3ea))

## [2.63.1](https://github.com/Flagsmith/flagsmith/compare/v2.63.0...v2.63.1) (2023-07-21)


### Bug Fixes

* **webhooks:** fix skipping webhooks calls on timeouts ([#2501](https://github.com/Flagsmith/flagsmith/issues/2501)) ([583e248](https://github.com/Flagsmith/flagsmith/commit/583e248cda58341b02ceeb5b75945550963a6dba))

## [2.63.0](https://github.com/Flagsmith/flagsmith/compare/v2.62.5...v2.63.0) (2023-07-21)


### Features

* **limits:** Add limits to features, segments and segment overrides ([#2480](https://github.com/Flagsmith/flagsmith/issues/2480)) ([d150c7f](https://github.com/Flagsmith/flagsmith/commit/d150c7f6c4b5e2336518b4dfba7895c61c2737a1))
* **tests:** test coverage ([#2482](https://github.com/Flagsmith/flagsmith/issues/2482)) ([1389c6e](https://github.com/Flagsmith/flagsmith/commit/1389c6eb8e39920fcc962c73c71fa096b902c260))

## [2.62.5](https://github.com/Flagsmith/flagsmith/compare/v2.62.4...v2.62.5) (2023-07-20)


### Bug Fixes

* **infra:** reduce number of threads per processor and increase sleep interval ([#2486](https://github.com/Flagsmith/flagsmith/issues/2486)) ([dd2516b](https://github.com/Flagsmith/flagsmith/commit/dd2516b222785dbc62003c9d054716f1c7d32e44))

## [2.62.4](https://github.com/Flagsmith/flagsmith/compare/v2.62.3...v2.62.4) (2023-07-19)


### Bug Fixes

* re-add EDGE_API_URL to api service task definition ([#2475](https://github.com/Flagsmith/flagsmith/issues/2475)) ([9554864](https://github.com/Flagsmith/flagsmith/commit/95548642edb40b5ec2fffdb6c1dcdab82a083181))

## [2.62.0](https://github.com/Flagsmith/flagsmith/compare/v2.61.0...v2.62.0) (2023-07-19)


### Features

* add descriptive event title to dynatrace integration ([#2424](https://github.com/Flagsmith/flagsmith/issues/2424)) ([f1dba53](https://github.com/Flagsmith/flagsmith/commit/f1dba5376b4bf1d2e9115f08998c8170678a8a80))


### Bug Fixes

* Allow signups when invited and in PREVENT_SIGNUP mode ([#2448](https://github.com/Flagsmith/flagsmith/issues/2448)) ([10719eb](https://github.com/Flagsmith/flagsmith/commit/10719ebb89eccb7bed83e5c43055d98c14724748))

## [2.61.0](https://github.com/Flagsmith/flagsmith/compare/v2.60.0...v2.61.0) (2023-07-16)


### Features

* Adjust AWS payment settings ([#2400](https://github.com/Flagsmith/flagsmith/issues/2400)) ([de4618d](https://github.com/Flagsmith/flagsmith/commit/de4618d02fbdffd774e7a34047590921c4c5bf4f))
* Bake enterprise version info into private cloud image ([#2420](https://github.com/Flagsmith/flagsmith/issues/2420)) ([acebf93](https://github.com/Flagsmith/flagsmith/commit/acebf939d80503d1b1fd964135646d06c7d0cb04))


### Bug Fixes

* (sales dashboard) correct api call overage data  ([#2434](https://github.com/Flagsmith/flagsmith/issues/2434)) ([c55e675](https://github.com/Flagsmith/flagsmith/commit/c55e675b023567b38e9750a3a5cc6b0a1859c209))
* ensure relevant email domains are not sent to Pipedrive ([#2431](https://github.com/Flagsmith/flagsmith/issues/2431)) ([3a4d8cb](https://github.com/Flagsmith/flagsmith/commit/3a4d8cbe8889389bbd7aefd9676f8c12cedf3c52))


### Documentation

* new architecture diagram ([#2433](https://github.com/Flagsmith/flagsmith/issues/2433)) ([2169340](https://github.com/Flagsmith/flagsmith/commit/21693404229f6705379be093c5a946f7bdcdda5f))
