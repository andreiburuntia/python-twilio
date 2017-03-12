import requests

r = requests.get("https://api.tfl.gov.uk/Line/Mode/tube/Status?detail=true&app_id=4a82146e&app_key=34d2c94c40646f4a7d268ed0276813dc")
print(r)