import cv2
import datetime
import time
import numpy as np



face_cascade = cv2.CascadeClassifier(r'C:\Users\Administrator\AppData\Local\
Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

startTime = datetime.datetime.now()

img = cv2.imread('tiao2.jpg')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #将图像转换为灰色

'''
x = y =200
w = 300
color = (0,0,255)
cv2.rectangle(gray_img,(x,y),(x+w,y+w),color,1)
'''

color=(0,255,0)

faceRects = face_cascade.detectMultiScale(
    gray_img,scaleFactor=1.2,minNeighbors=3,minSize=(32,32),flags=cv2.CASCADE_SCALE_IMAGE)
if len(faceRects):
    for faceRect in faceRects:
        x,y,w,h = faceRect
        cv2.rectangle(img, (x, y), (x + h, y + w), color, 2)
         # 左眼
        cv2.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                       color)
         #右眼
        cv2.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                       color)
         #嘴巴
        cv2.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                          (x + 5 * w // 8, y + 7 * h // 8), color)

        
endTime = datetime.datetime.now()
print((endTime - startTime))
cv2.imshow('Image',img)  #显示图像
cv2.waitKey(0)
cv2.destroyAllWindows() #释放窗体资源

