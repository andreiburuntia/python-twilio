import requests
import json
import re

url = "https://maps.googleapis.com/maps/api/directions/json"

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

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
querystring = {"origin": "Stratford", "destination": "plaistow", "mode": "driving", "region": "uk",
               "key": "AIzaSyAs329pghB3CSydeUeFhvpMWK2EWtJSxXw"}
response = requests.request("GET", url, headers=headers, params=querystring)
distance=response.json()["routes"][0]["legs"][0]["distance"]["text"]
duration=response.json()["routes"][0]["legs"][0]["duration"]["text"]
directions=[]
directions_pretty=""
count=1
for step in response.json()["routes"][0]["legs"][0]["steps"]:
    directions.append((cleanhtml(step["html_instructions"])))
    directions_pretty+=str(count)+". "+cleanhtml(step["html_instructions"])+"\n\n"
    count+=1
print (directions_pretty)
#print(response.json()["routes"][2]["legs"][0]["steps"][0]["distance]"]["text"])