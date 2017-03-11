from flask import Flask, request, redirect
from twilio import twiml

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = twiml.Response()

    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")

    return str(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
