from flask import Flask, request, redirect
import twilio.twiml
import datetime
import requests
import googlemaps
from weather import pretty_print_weather
from gmaps import fetch_directions
from twilio import twiml
from tfl import status
from gmaps import pretty_print_directions
import re

app = Flask(__name__)

import requests
# @app.route("/sms", methods=['GET', 'POST'])
# def hello_monkey():
#     """Respond to incoming calls with a simple text message."""
#
#     resp = twiml.Response()
#     resp.message("Hello, Mobile Monkey")
#     return str(resp)




def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


url = "https://maps.googleapis.com/maps/api/directions/json"

headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
    'x-chrome-uma-enabled': "1",
    'x-client-data': "CIm2yQEIpLbJAQjBtskBCKiKygEI+5zKAQipncoB",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'dnt': "1",
    'accept-encoding': "gzip, deflate, sdch, br",
    'cache-control': "no-cache"
}


# @app.route("/sms", methods=['GET', 'POST'])
# def hello_monkey():
#     """Respond to incoming calls with a simple text message."""
#
#     resp = twiml.Response()
#     resp.message("Hello, Mobile Monkey")
#     return str(resp)


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
            s = body
            start_loc = s[s.find("(") + 1:s.find(")")]
            a = s.split(",")[1]
            end_loc = a[a.find("(") + 1:a.find(")")]
            querystring = {"origin": start_loc, "destination": end_loc, "mode": "driving", "region": "uk",
                           "key": "AIzaSyAs329pghB3CSydeUeFhvpMWK2EWtJSxXw"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            distance = response.json()["routes"][0]["legs"][0]["distance"]["text"]
            duration = response.json()["routes"][0]["legs"][0]["duration"]["text"]
            directions = []
            directions_pretty = ""
            count = 1
            for step in response.json()["routes"][0]["legs"][0]["steps"]:
                directions.append((cleanhtml(step["html_instructions"])))
                directions_pretty += str(count) + ". " + cleanhtml(step["html_instructions"]) + "\n"
                count += 1
            resp.message("Distance: " + distance + "\nDuration: " + duration + "\nSteps:\n" + directions_pretty)

        elif arguments[0] == 'Weather':
            resp.message(pretty_print_weather(body.split(" ")[1]))
        elif arguments[0] == 'Tfl':
            resp.message(status(body.split(" ")[1]))
        else:
            resp.message("Usage:\n"
                         +"Location (<loc 1>), (<loc 2>) -> directions\n"
                         +"Weather <location> -> weather\n"
                         +"Tfl <line> -> service status for an underground line\n")
    return str(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
