import requests
import json
api_key = "pqA9vO_M8eeo7mfl8H023i6K9GiSv1we"
api_secret = "0CBwd83rZWdmQEwvhjheaJdixQ-yeNWB"
urls = " https://api-cn.faceplusplus.com/facepp/v3/faceset/delete"

datag = {
    "api_key": api_key,
    "api_secret": api_secret,
    "outer_id": "QUST2019director",
    "check_empty":0
}


r = requests.post(url=urls,data=datag)

print(json.loads(r.text))

