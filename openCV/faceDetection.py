# encoding:utf-8
import cv2
import numpy as np
 
def main():
    detectFaces('2.jpg')
    detectEyes('wolf.jpg')

def detectFaces(img_path):    
    face_cascade = cv2.CascadeClassifier(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

    # 读取图像
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 检测脸部
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=10,
        minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE)

    #画正方形标记人脸
    for (x, y, w, h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    print('Detected ', len(faces), " face")
        

    cv2.imshow('img', img)
    cv2.imwrite('faceDetect.jpg',img)

    while True:
        if cv2.getWindowProperty('img', 0) == -1: #当窗口关闭时为-1，显示时为0
            break
        cv2.waitKey(1)

    cv2.destroyAllWindows() #释放窗体资源
  

def detectEyes(img_path):
    face_cascade = cv2.CascadeClassifier(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    eye_cascade = eye_cascade = cv2.CascadeClassifier(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_eye.xml')   

    # 读取图像
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=10,
        minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x,y,w,h) in faces:
        roi_gray = gray[y: y + h, x: x + w]
        roi_color = img[y: y + h, x: x + w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray,scaleFactor=1.2,minNeighbors=5)
    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    cv2.imwrite('eyeDetect.jpg',img)
    while True:
        if cv2.getWindowProperty('img', 0) == -1: #当窗口关闭时为-1，显示时为0
            break
        cv2.waitKey(1)

    cv2.destroyAllWindows() #释放窗体资源
  

    


if __name__ == '__main__':
    main()