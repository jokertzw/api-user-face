import requests
import json
api_key = "pqA9vO_M8eeo7mfl8H023i6K9GiSv1we"
api_secret = "0CBwd83rZWdmQEwvhjheaJdixQ-yeNWB"
urls = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getfacesets"
urld = "https://api-cn.faceplusplus.com/facepp/v3/faceset/getdetail"
datag = {
    "api_key": api_key,
    "api_secret": api_secret,
}
datad = {
    "api_key": api_key,
    "api_secret": api_secret,
    "outer_id":"董玉颖.jpg"
}

r = requests.post(url=urls,data=datag)
r2 = requests.post(url=urld,data=datad)
print(json.loads(r.text))
print(json.loads(r2.text))