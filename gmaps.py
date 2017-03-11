import googlemaps
from datetime import datetime
import json
import re
from twilio.rest import TwilioRestClient

mykey='AIzaSyDvcfhT988-hv6TFsMey1K_q84hfAh9Nm8'
gmaps = googlemaps.Client(key='AIzaSyDvcfhT988-hv6TFsMey1K_q84hfAh9Nm8')

start='manchaster airport'
end='mediacityuk'

directions_result=gmaps.directions(start,end,mode="driving",departure_time=datetime.now())
with open('data.txt', 'w') as outfile:
    json.dump(directions_result,outfile)

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

directions_list=[]

for single_direction in directions_result[0]['legs'][0]['steps']:
    directions_list.append(cleanhtml(single_direction['html_instructions']))
    print (cleanhtml(single_direction['html_instructions']))

account_sid = "AC9a8405724afb8b609912054251250dda" # Your Account SID from www.twilio.com/console
auth_token  = "a9658b8cea6a3daa57c62583e8256840"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from Python",
    to="+447375531812",    # Replace with your phone number
    from_="+442033899587") # Replace with your Twilio number

print(message.sid)