from Serch_img import serchimg
import time
import dui_lie as d
import threading
import cv2


#打开http服务器
import httpse as h
ser = threading.Thread(target=h.init, args=())
ser.start()
###调用电脑摄像头检测人脸并截图


# api_key = "pqA9vO_M8eeo7mfl8H023i6K9GiSv1we"
# api_secret = "0CBwd83rZWdmQEwvhjheaJdixQ-yeNWB"
# urldec = "https://api-cn.faceplusplus.com/facepp/v3/detect"
# datadec = {
#     "api_key": api_key,
#     "api_secret": api_secret,
#     "outer_id":"AQUST2019",
#     "return_attributes":'facequality'
# }
num = 0
def CatchPICFromVideo(window_name, camera_idx, path_name):
    cv2.namedWindow(window_name)
    global num#统计拍照的次数
    #视频来源，可以来自一段已存好的视频，也可以直接来自USB摄像头
    cap = cv2.VideoCapture(camera_idx)

    #告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

    #识别出人脸后要画的边框的颜色，RGB格式, color是一个不可增删的数组
    color = (0, 255, 0)

    while cap.isOpened():
        time.sleep(0.5)
        ok, frame = cap.read() #读取一帧数据
        if not ok:
            break

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #将当前桢图像转换成灰度图像

        #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        # print('opencv:',time.time())
        if len(faceRects) > 0:          #大于0则检测到人脸
            for faceRect in faceRects:  #单独框出每一张人脸
                x, y, w, h = faceRect

                #将当前帧保存为图片
                img_name = "%s/%d.jpg" % (path_name, num)
                # print(img_name)
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                try:
                    cv2.imwrite(img_name, image,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])
                    # print('serchimg:', time.time())
                    #开启线程
                    serch = threading.Thread(target=serchimg, args=(img_name,d.q))
                    serch.start()
                    # serch.join()

                    num += 1
                    #
                    # if num > (catch_pic_num):   #如果超过指定最大保存数量退出循环
                    #     cap.release()
                    #     cv2.destroyAllWindows()

                    #画出矩形框
                    cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                    #显示当前捕捉到了多少人脸图片了，这样站在那里被拍摄时心里有个数，不用两眼一抹黑傻等着
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    # cv2.putText(frame,'num:%d/100' % (num),(x + 30, y + 30), font, 1, (255,0,255),4)

                    #超过指定最大保存数量结束程序
                except BaseException:
                    position = 1


        #显示图像
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

            #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()


def fun1():
    global num
    # print(num)
path = "zy.jpg"
if __name__ == '__main__':
    # pool = Pool(5)  # 创建一个5个进程的进程池
    #
    # pool.apply_async(func=CatchPICFromVideo,args=("get face", 0, 20, "image"))
    #
    # pool.apply_async(func=fun1)

    CatchPICFromVideo("get face", 1,"image")
    # for i in range(5):  # 开启5个子进程执行fun1函数
