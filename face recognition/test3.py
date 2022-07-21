# encoding:utf-8
import cv2
import numpy as np
 
# 运行之前，检查cascade文件路径是否在相应的目录下
face_cascade = cv2.CascadeClassifier(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_eye.xml')
 
# 读取图像
img = cv2.imread('ning3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# 检测脸部
faces = face_cascade.detectMultiScale(
    gray, scaleFactor=1.01, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
print('Detected ', len(faces), " face")
 
for face in faces:
    x,y,w,h = face
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y: y + h, x: x + w]
    roi_color = img[y: y + h, x: x + w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
 
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
