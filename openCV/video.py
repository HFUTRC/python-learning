import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)    # 参数0表示获取第一个摄像头
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。
    #frame就是每一帧的图像，是个三维矩阵。
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('Video',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()