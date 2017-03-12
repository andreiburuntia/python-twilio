from flask import Flask, request, redirect
from twilio import twiml

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = twiml.Response()

    if body is not None:
        arguments = body.split("\s")

        if arguments[0] == 'location':
            s=body
            start_loc=s[s.find("(")+1:s.find(")")]
            a=s.split(",")[1]
            end_loc=a[a.find("(")+1:a.find(")")]
            resp.message(start_loc+" - "+end_loc)

        elif arguments[0] == 'twitter':
            resp.message("Hi -1!")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
