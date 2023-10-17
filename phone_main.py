import cv2
from cvzone.PoseModule import PoseDetector
import send
import os
import send_mms
import requests 
import numpy as np 
import imutils 
url = "http://192.168.1.19:8080/shot.jpg"
path = r'C:\xampp\htdocs\tmp'
detector=PoseDetector()
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
l=[]
flag=True
while True:
    img_resp = requests.get(url) 
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
    img = cv2.imdecode(img_arr, -1) 
    img = imutils.resize(img, width=1000, height=1800) 
    img=detector.findPose(img)
    imlist,bbox=detector.findPosition(img)
    if len(imlist) > 0:
        print("Human Detect")
        l.append(1)
    if len(l) > 5 and flag:
        flag=False
        send.sendSms()
        os.chdir(path)
        img_resp = requests.get(url) 
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1) 
        cv2.imwrite("image1.png", img)
        send_mms.send_mms()
        break
    cv2.imshow("Output",img)
    q=cv2.waitKey(1)
    if q==ord('q'):
        break