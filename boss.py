#用到的wheel
import face_recognition
import cv2
import os
import jpush as jpush
from jpush import common


#欢迎信息
print('-'*20,'欢迎使用boss来了系统','-'*20)

#提示信息
print('亲，你想干什么呢：')
print('\t1.开始监控boss')
print('\t2.误点，退出吧')
print('\t3.显示帮助信息')
 
#功能选择
function_choose = input('请选择：')

#分割线
print('-'*60)

#判断变量,控制后面功能的实施
torf = 1
name = "Unknown"

#功能模块
if function_choose=='1':
    print('你选择了1，即将开始监控boss')
    

elif function_choose=='2':
    print('拜拜')
    torf = 0

elif function_choose=='3':
    with open('help.txt','r',encoding='UTF-8') as f:  # 打开指定文本
        text_new = f.read()  # 读取文本数据
        print(text_new)
#    with open('D:/python/face/help.txt','r',encoding='gbk') as f:
#        print(f.read())

else:
    print('请输入有效指令。')
    print('将默认退出，拜拜。')
    torf = 0

#人脸识别模块功能实现
#使用摄像头
video_capture = cv2.VideoCapture(0)

while torf:
    #加载boss图像并识别
    boss_image = face_recognition.load_image_file("boss.jpg")
    boss_face_encoding = face_recognition.face_encodings(boss_image)[0]

    # 抓取一帧视频
    ret, frame = video_capture.read()

    # 在视频帧中查找所有面和面编码
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # 在这个视频帧的每个面上循环
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # 判断是否为指定人像
        match = face_recognition.compare_faces([boss_face_encoding], face_encoding,tolerance=0.5)
        #####
        if match[0]:
            name = "Boss"
            os.startfile('tishi.mp3')
            print('boss来了')
            torf=0
            break


        # 在脸上画一个方框
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # 添加姓名标签
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # 结果图像
    cv2.imshow('Video', frame)


    # 按 ‘q’ 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#if name == "Boss":
 #   print('boss来了')
  #  os.startfile('tishi.mp3')

#关闭摄像头
video_capture.release()
cv2.destroyAllWindows()