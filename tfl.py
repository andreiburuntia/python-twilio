import requests
import json

r = requests.get("https://api.tfl.gov.uk/Line/Mode/tube/Status?detail=true&app_id=4a82146e&app_key=34d2c94c40646f4a7d268ed0276813dc")

def status(req):
    for num in range(0,11):
        if req.lower() in r.json()[num]["name"].lower():
            return  r.json()[num]["lineStatuses"][0]["statusSeverityDescription"]



# returnResult("Central")