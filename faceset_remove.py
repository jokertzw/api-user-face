import requests
import json
api_key = "i4efjO8MKkW5QwxOoqHGlWfFqxGLk_eG"
api_secret = "ZHSvAQxSwakKRXeeH1pFwhD1Tpx1CDmU"
urls = " c69cb459389275ec91d9cbcd0f0d4438"

datag = {
    "api_key": api_key,
    "api_secret": api_secret,
}


r = requests.post(url=urls,data=datag)

print(json.loads(r.text))

