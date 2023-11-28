import contactUsSlack from './contact-us-slack';
import dataRelay from 'data-relay/dist/node';
const isProduction = process.env.VERCEL_ENV === 'production'
export default function(requestBody) {
    if(!isProduction) {
        return []
    }
    switch (requestBody.name) {
        case 'Contact Form':
        default: {
            return [
                contactUsSlack(requestBody.data),
                dataRelay
                    .sendEvent(
                        requestBody.data,
                        { apiKey: process.env.DATA_RELAY_API_KEY },
                    )
            ]
        }
    }
}
