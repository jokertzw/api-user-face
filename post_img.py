import requests
import json
filename = "one.jpg"
filepath1 = "C:\\Users\\23584\\PycharmProjects\\face++\\Face++test\\one.jpg"
filepath2 = "C:\\Users\\23584\\PycharmProjects\\face++\\Face++test\\王明超.jpg"
files={
    "image_file1": open(filepath1, 'rb').read(),
    "image_file2": open(filepath2, 'rb').read()
}
# print(open(filepath1,'rb').read())
data = {
    "image_base64_1": open(filepath1,'rb').read(),
    "image_base64_2	": open(filepath2,'rb').read(),
    "test" : 1
}
img1 = open(filepath1,'rb').read()
img2 = open(filepath2,'rb').read()
url = "https://api-cn.faceplusplus.com/facepp/v3/compare?" +\
      "api_key=zppJzy9Z4dF8zF4zvpyfkxOkINB89gJH&" +\
      "api_secret=sXpOujfZnWm5WnplNhhMkPCwpkGQkg9S&"

print(data)
r = requests.post(url = url,files=files )
# 将其转换成字典型
confidence = json.loads(r.text)
# print(r.text)
# print(json.loads(r.text))
# 得出相似度
print(json.loads(r.text)["confidence"])
