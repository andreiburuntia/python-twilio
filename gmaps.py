import googlemaps
from datetime import datetime
import json
import re
from twilio.rest import TwilioRestClient

# hardcoded, from twilio.com/console or whatever
mykey = 'AIzaSyDvcfhT988-hv6TFsMey1K_q84hfAh9Nm8'
gmaps = googlemaps.Client(key='AIzaSyDvcfhT988-hv6TFsMey1K_q84hfAh9Nm8')


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def fetch_directions(start, end, mode, departure_time):
    result_tuple = ()
    directions_list = []
    directions_result = gmaps.directions(
        start, end, mode=mode, departure_time=departure_time)
    result_tuple += (directions_result[0]['legs'][0]['distance']['text'], )
    result_tuple += (directions_result[0]['legs'][0]['duration']['text'], )
    for single_direction in directions_result[0]['legs'][0]['steps']:
        directions_list.append(
            cleanhtml(single_direction['html_instructions']))

    result_tuple += (directions_list, )
    # tuple of ("distance","duration",[list of directions])
    return result_tuple


def send_sms(content, to_number, from_number):
    # Your Account SID from www.twilio.com/console
    account_sid = "AC9a8405724afb8b609912054251250dda"
    # Your Auth Token from www.twilio.com/console
    auth_token = "a9658b8cea6a3daa57c62583e8256840"

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(body=content,
                                     to=to_number,    # Replace with your phone number
                                     from_=from_number)  # Replace with your Twilio number


def concat_with_new_line(tuple):
    count = 1
    result = ""
    result += "Distance: " + tuple[0] + "\n\n"
    result += "Duration: " + tuple[1] + "\n\n"
    for single_direction in tuple[2]:
        single_direction = single_direction.replace(
            "&amp;", "&")  # escape weird char
        single_direction = single_direction.replace(
            "⛉ ", "")  # escape weird char
        result += str(count) + ". " + single_direction + "\n\n"
        count += 1
    return result

# main


test_directions = fetch_directions(
    "manchester airport", "manchester mediacityuk", "driving", datetime.now())
test_content = concat_with_new_line(test_directions)
# print(test_content)
send_sms(test_content,"+447375531812","+442033899587")
