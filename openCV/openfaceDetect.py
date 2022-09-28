import threading
import cv2
import os
import openface
import dlib

import time


fileDir = os.path.dirname(os.path.realpath(__file__))
modelDir = os.path.join(fileDir, 'models')
dlibModelDir = os.path.join(modelDir, 'dlib')


align = openface.AlignDlib(os.path.join(dlibModelDir, "shape_predictor_68_face_landmarks.dat"))

class OpcvCapture(threading.Thread):
    def __init__(self, win_name, cam_name):
        super().__init__()
        self.cam_name = cam_name
        self.win_name = win_name

    def run(self):
        capture = cv2.VideoCapture(0)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) #宽度 
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) #高度
        capture.set(cv2.CAP_PROP_FPS, 30); #帧率 帧/秒

        
        #fps =capture.get(cv2.CAP_PROP_FPS) #获取视频帧数
        cv2.namedWindow(self.win_name)
        while (True):
            # 获取一帧
            start = time.time()
            ret, frame = capture.read()
            count = 0
            
            if (count % 3 == 0):
                show_img = self._detector(frame, mirror=True)
                cv2.imshow(self.win_name, show_img)
            else:
                cv2.imshow(self.win_name,frame)

            count+=1

            if(count>300):
                count = 0
            
            
            end = time.time()
            second = end-start
            print("耗时 {} s.".format(second))
            # fps = 1/second
            # print("帧率：{}".format(fps))
            
            if cv2.waitKey(1) & 0xff == ord('q'):
                break

    def _detector(self, frame, mirror=False):
        show_img = cv2.flip(frame, flipCode=1) if mirror else frame

        # 获取所有的脸
        rects = align.getAllFaceBoundingBoxes(show_img)
        for rect in rects:

            # draw_1 = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)    画框
            cv2.rectangle(show_img,(rect.left(),rect.top()),(rect.right(),rect.bottom()),(0,255,0),2)

            # 获取特征点
            # bb = align.findLandmarks(show_img, rect)
            # for pt in bb:
                # cv2.circle(show_img, pt, 3, [0, 0, 255], thickness=-1)
        return show_img

if __name__ == "__main__":
    camera1 = OpcvCapture("camera1", 1)
    camera1.start()
