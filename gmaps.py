import googlemaps
from datetime import datetime
import re

gmaps = googlemaps.Client(key='AIzaSyDvcfhT988-hv6TFsMey1K_q84hfAh9Nm8')


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def fetch_directions(start_location, end_location):
    directions_list = []
    directions_result = gmaps.directions(start_location, end_location, mode="driving", departure_time=datetime.now())
    directions_list.append(directions_result[0]['legs'][0]['distance']['text'])
    directions_list.append(directions_result[0]['legs'][0]['duration']['text'])
    for single_direction in directions_result[0]['legs'][0]['steps']:
        directions_list.append(
            cleanhtml(single_direction['html_instructions']))

    return directions_list


def pretty_print_directions(start_location, end_location):
    print ("pretty print dirs")
    pretty_list = fetch_directions(start_location, end_location)
    print ("done")
    count = 1
    result = ""
    print(pretty_list)
    result += "Distance: " + pretty_list[0] + "\n\n"
    result += "Duration: " + pretty_list[1] + "\n\n"
    for i in range(2, len(pretty_list)):
        result += str(count) + ". " + pretty_list[i] + "\n\n"
        count += 1
    return result

