import requests

import json
import os

filename = "one.jpg"
path1 = "C:\\Users\\23584\\PycharmProjects\\face++\\Face++test\\director\\"
files = {}
api_keyt = "zppJzy9Z4dF8zF4zvpyfkxOkINB89gJH"
api_secrett = "sXpOujfZnWm5WnplNhhMkPCwpkGQkg9S"
api_key = "pqA9vO_M8eeo7mfl8H023i6K9GiSv1we"
api_secret = "0CBwd83rZWdmQEwvhjheaJdixQ-yeNWB"
urls = "https://api-cn.faceplusplus.com/facepp/v3/search"
datas = {
    "api_key": api_key,
    "api_secret": api_secret,
    "outer_id":"QUST2019director",
    "return_result_count":5
}
def serchimg(filename):
    files["image_file"] = open(filename, 'rb').read()
    r = requests.post(url=urls, files=files, data=datas)
    print(r.text)
    # for name in json.loads(r.text)["results"]:
    #     print(name["user_id"])
    return(json.loads(r.text)["results"][0]["user_id"])



