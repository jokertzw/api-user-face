import requests
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

import time

import base64

# from queue import Queue
#
# q =Queue()

import threading
from TTS import speak
#http协议


data = {}
host = ('localhost', 8888)
class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())


filename = "zhr.jpg"
files = {}
api_keyt = "zppJzy9Z4dF8zF4zvpyfkxOkINB89gJH"
api_secrett = "sXpOujfZnWm5WnplNhhMkPCwpkGQkg9S"
api_key = "pqA9vO_M8eeo7mfl8H023i6K9GiSv1we"
api_secret = "0CBwd83rZWdmQEwvhjheaJdixQ-yeNWB"
urls = "https://api-cn.faceplusplus.com/facepp/v3/search"

datas = {
    "api_key": api_key,
    "api_secret": api_secret,
    "outer_id":"AQUST2019",
    "return_result_count":5
}
urldec = "https://api-cn.faceplusplus.com/facepp/v3/detect"
datadec = {
    "api_key": api_key,
    "api_secret": api_secret,
    "outer_id":"AQUST2019",
    "return_attributes":'facequality'
}
datasend = {}
datasend['already'] = []
datajson = ''



# 线程锁
# lock = threading.Lock()
# already = ['王明超同学']
def serchimg(filename,q):
    files["image_file"] = open(filename, 'rb').read()
    try:
        rd = requests.post(url=urldec, files=files, data=datadec)
        # print(rd.text)

        #人脸质量
        zhixin = json.loads(rd.text)["faces"][0]["attributes"]["facequality"]

        facetaken = json.loads(rd.text)["faces"][0]["face_token"]
        # print(facetaken)
        # print(zhixin["threshold"])
        # print(zhixin["value"])
        # return 0
        if zhixin["threshold"]<zhixin["value"]:
            datas["face_token"] = facetaken
            r = requests.post(url=urls, data=datas)
            # print(r.text)

            # return 0
            # for name in json.loads(r.text)["results"]:
            #     print(name["user_id"])

            # print(json.loads(r.text)["results"][0]["confidence"])
            if(json.loads(r.text)["results"][0]["confidence"]>70):
                text = json.loads(r.text)["results"][0]["user_id"]
                # print(text)

                # # code = u+text[0]
                # # text[0] = text[0].decode('unicode_escape')
                # print(text[0])
                # print(text[0] not in already)

                # if text[0] not in already:

                if text not in datasend['already']:
                    name = text.split('.')
                    # lock.acquire()
                    datasend['already']=text
                    # print(datasend['already'])
                    # lock.release()
                    print(name[0])
                    speaknam = "欢迎" + name[0] + '入场'
                    with open(filename, "rb") as img:
                        datasend['img'] = base64.b64encode(img.read())
                        #把读取出来的bytes类型转换为str
                        datasend['img'] = str(datasend['img'])[2:-1]
                    #获得音频
                    datasend['audio'] = speak(speaknam)
                    # print(datasend['audio'])
                    # print('httpsend:', time.time())
                    # print(datasend)
                    # print(type(datasend['audio']))
                    q.put(datasend)
                    q.put(datasend)
                    # print('队列',q.get())
                    # datajson = json.dumps(datasend)
                    # print(type(datajson))
                        # print(datasend['img'])
                        # print(type(datasend['img']))
                    # task_process(speak)
                    # print(datasend)
                    #
                    # with open('../face++/wav/'+'欢迎'+text[0]+'入场'+'.wav', "rb") as speak:
                    #     datasend['speak'] = base64.b64encode(speak.read())

                    # print(datasend)
                    # h.data['wav'] = open('../face++/wav/'+'欢迎'+text[0]+'入场'+'.wav','rb').read()
                    # h.data['name'] = open('../face++/Face++test/sendImg/'+text[0]+'.'+text[1],'rb').read()


                    # print(data['wav'])
                    # print(data['name'])
                    # 打开网页的方法
                    # web_url = '127.0.0.1:2222/'+speak
                    # chrome_path = r'D:\\360se6\\Application\\360se.exe'  # 浏览器路径
                    # webbrowser.register('360', None, webbrowser.BackgroundBrowser(chrome_path))
                    # webbrowser.get('360').open(web_url,new=0,autoraise = False)


                    # if len(already) > 5:
                    #     already = already[4:5]
                # else:
                    # print('已经入场')
    except BaseException:
        # print("查无此人")
        mmm =1

#
# serchimg(filename)
#
#
# serchimg(filename)
#
