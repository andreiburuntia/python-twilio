from flask import Flask, request, redirect
import twilio.twiml
import datetime
import gmaps
from twilio import twiml

app = Flask(__name__)


# @app.route("/", methods=['GET', 'POST'])
# @app.route("/sms", methods=['GET', 'POST'])
# def hello_monkey():
#     """Respond to incoming calls with a simple text message."""
#
#     resp = twiml.Response()
#     resp.message("Hello, Mobile Monkey")
#     return str(resp)


def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    body = body.upper()
    # Start our TwiML response
    resp = twiml.Response()

    if body is not None:
        arguments = body.split(" ")
        if arguments[0] == 'Location':
            # s=body
            # start_loc=s[s.find("(")+1:s.find(")")]
            # a=s.split(",")[1]
            # end_loc=a[a.find("(")+1:a.find(")")]
            # directions=gmaps.fetch_directions(start_loc,end_loc,"driving",datetime.now())
            # response_content=gmaps.concat_with_new_line(directions)
            # resp.message(str(response_content))
        # elif arguments[0] == 'Twitter':
            resp.message("Hi -1!")

    return str(resp)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    # Start our TwiML response
    resp = twiml.Response()

     if body is not None:
        arguments = body.split(" ")
        if arguments[0] == 'Location':
            s=body
            start_loc=s[s.find("(")+1:s.find(")")]
            a=s.split(",")[1]
            end_loc=a[a.find("(")+1:a.find(")")]
            directions=gmaps.fetch_directions(start_loc,end_loc,"driving",datetime.now())
            response_content=gmaps.concat_with_new_line(directions)
            resp.message(str(response_content))

        elif arguments[0] == 'Twitter':
            resp.message("Hi -1!")

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
