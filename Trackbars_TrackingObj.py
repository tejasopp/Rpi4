import cv2
from picamera2 import Picamera2
import numpy as np
import time
piCam=Picamera2()
def Trackhl(val):
    global heuLow
    heuLow = val
def Trackhh(val):
    global heuHigh
    heuHigh = val
def Tracksl(val):
    global satLow
    satLow = val
def Tracksh(val):
    global satHigh
    satHigh = val
def Trackvl(val):
    global valLow
    valLow = val
def Trackvh(val):
    global valHigh
    valHigh = val
disph=720
dispw=1280
piCam.preview_configuration.main.size=(dispw,disph)
piCam.preview_configuration.main.format="RGB888"
piCam.preview_configuration.controls.FrameRate=30
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()
fps=0
pos=(30,60)
font=cv2.FONT_HERSHEY_SIMPLEX
height=1.5
myColor=(0,0,255)
weight=3
cv2.namedWindow('My Trackbars')
cv2.createTrackbar('heu Low','My Trackbars',0,179,Trackhl)
cv2.createTrackbar('heu High','My Trackbars',0,179,Trackhh)
cv2.createTrackbar('sat Low','My Trackbars',100,255,Tracksl)
cv2.createTrackbar('sat High','My Trackbars',255,255,Tracksh)
cv2.createTrackbar('val Low','My Trackbars',100,255,Trackvl)
cv2.createTrackbar('val High','My Trackbars',255,255,Trackvh)
heuLow =0
heuHigh=0
satLow=100
satHigh=255
valLow=100
valHigh=255
while True:
    tStart=time.time()
    frame=piCam.capture_array()
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerbound=np.array([heuLow,satLow,valLow])
    upperbound=np.array([heuHigh,satHigh,valHigh])
    myMask=cv2.inRange(frameHSV,lowerbound,upperbound)
    myMaskSmall=cv2.resize(myMask,(int(dispw/2),int(disph/2)))
    ObjectOfinterest=cv2.bitwise_and(frame,frame,mask=myMask)
    ObjectOfinterestSmall=cv2.resize(ObjectOfinterest,(int(dispw/2),int(disph/2)))
    #print(frameHSV[int(disph/2),int(dispw/2)])
    cv2.putText(frame,str(int(fps)),pos,font,height,myColor,weight)
    cv2.imshow("frame",frame)
    cv2.imshow("TrackingMask",myMaskSmall)
    cv2.imshow("Tracking",ObjectOfinterestSmall)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps = .9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()