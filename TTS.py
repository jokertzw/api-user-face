import Serch_img as S
import requests
import time
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.cvm.v20170312 import cvm_client, models
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDXtztXtxHbfSfWBfmkTw71mJZfV4M9Bow", "NTUfhMs04MVWgh7PVXQ8jAc4aKxSo28E")

    # 实例化要请求产品(以cvm为例)的client对象
    client = cvm_client.CvmClient(cred, "ap-shanghai")

    # 实例化一个请求对象
    req = models.DescribeZonesRequest()

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeZones(req)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)


'''
timestamp : int(time.time()) 这个是时间戳


'''
# url = "https://tts.cloud.tencent.com/stream"
#
# def tts_wav_demo():
#     url = "https://tts.cloud.tencent.com/stream"
#     header = {
#         "Content-Type": "application/json",
#         "Authorization": "VVerIEkz2OAuSBdNtH6W2M1xal0="
#     }
#     request_data = {
#         "AppId": 1255824371,
#         "SecretId": "AKIDXtztXtxHbfSfWBfmkTw71mJZfV4M9Bow",
#         # "SecretKey":"NTUfhMs04MVWgh7PVXQ8jAc4aKxSo28E",
#         "PrimaryLanguage": 1,
#         "SampleRate": 16000,
#         "Action": "TextToVoice",
#         "VoiceType": 1,
#         "Text": "我只是拿来测试的文本",
#         "SessionId": "session-1234",
#         "Timestamp": 1535362116,
#         "Expired": 1535365716,
#         "Speed": 0,
#         "Volume": 0
#     }
#     r = requests.post(url=url, headers=header, data=request_data)
#     print(r.text)
#
#
# if __name__ == '__main__':
#     # filename = "test.png"
#     # name = S.serchimg(filename)
#     # name = name.split(".")[0]
#     tts_wav_demo()
#     # print(name)