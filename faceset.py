import requests

import json
import os

filename = "one.jpg"
path1 = "C:\\Users\\23584\\PycharmProjects\\face++\\Face++test\\director\\"
files1 = os.listdir(path1)
files = {}
api_keyt = "zppJzy9Z4dF8zF4zvpyfkxOkINB89gJH"
api_secrett = "sXpOujfZnWm5WnplNhhMkPCwpkGQkg9S"
api_key = "pqA9vO_M8eeo7mfl8H023i6K9GiSv1we"
api_secret = "0CBwd83rZWdmQEwvhjheaJdixQ-yeNWB"

# for filepath in files1:
#     files["image_file"] = open(path1+filepath,'rb').read()
#     print(path1+filepath)
# print(files)

# filepath1 = "C:\\Users\\23584\\PycharmProjects\\face++\\Face++test\\one.jpg"
# filepath2 = "C:\\Users\\23584\\PycharmProjects\\face++\\Face++test\\王明超.jpg"
# files={
#     "image_file1": open(filepath1, 'rb').read(),
#     "image_file2": open(filepath2, 'rb').read()
# }
# # print(open(filepath1,'rb').read())
#
urldec = "https://api-cn.faceplusplus.com/facepp/v3/detect"
url_userid = "https://api-cn.faceplusplus.com/facepp/v3/face/setuserid"
urlfaceset = "https://api-cn.faceplusplus.com/facepp/v3/faceset/create"
datad = {
    "api_key":api_key,
    "api_secret":api_secret,
}
data_userid = {
    "api_key": api_key,
    "api_secret": api_secret,
}

# outer_id定义faceset库名
dataface = {
    "api_key": api_key,
    "api_secret": api_secret,
    "outer_id":"QUST2019director",
    "force_merge":1,
}

for filepath in files1:
    print(path1 + filepath)
    files["image_file"] = open(path1 + filepath, 'rb').read()
    r = requests.post(url=urldec, files=files,data=datad)
    faceset_token = json.loads(r.text)["faces"][0]['face_token']
    # dataface["user_data"] = filepath
    dataface["face_tokens"] = faceset_token
    data_userid["face_token"] = faceset_token
    data_userid["user_id"] = filepath
    rset = requests.post(url=urlfaceset, data=dataface)
    r_userid=requests.post(url=url_userid,  data=data_userid)

    print(rset.text)
    print(r_userid.text)
    # print(faceset_token)
    # print(type(faceset_token))


# 将其转换成字典型
# confidence = json.loads(r.text)
# print(r.text)
# print(json.loads(r.text))
