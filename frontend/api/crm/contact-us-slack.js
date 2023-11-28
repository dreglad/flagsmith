const SLACK_TOKEN = process.env.SLACK_TOKEN
const slackClient = SLACK_TOKEN && require('./slack-client')

export default function(data) {
    if(!SLACK_TOKEN) return Promise.resolve()

    const message = `New Contact Us form!
Name: ${data.message}
Email: ${data.email}
Phone: ${data.phone}
Message: ${data.message}
`
    return slackClient(message, 'contact-sales')
}
