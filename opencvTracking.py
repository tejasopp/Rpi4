import cv2
from picamera2 import Picamera2
import numpy as np
import time
piCam=Picamera2()
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
heuLow=68
heuHigh=113
satLow=100
satHigh=255
valLow=100
valHigh=255
lowerbound=np.array([heuLow,satLow,valLow])
upperbound=np.array([heuHigh,satHigh,valHigh])
while True:
    tStart=time.time()
    frame=piCam.capture_array()
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    myMask=cv2.inRange(frameHSV,lowerbound,upperbound)
    myMaskSmall=cv2.resize(myMask,(int(dispw/2),int(disph/2)))
    ObjectOfinterest=cv2.bitwise_and(frame,frame,mask=myMask)
    ObjectOfinterestSmall=cv2.resize(ObjectOfinterest,(int(dispw/2),int(disph/2)))
    #print(frameHSV[int(disph/2),int(dispw/2)])
    cv2.putText(frame,str(int(fps)),pos,font,height,myColor,weight)
    cv2.imshow("frame",frame)
    cv2.imshow("TrackingBlueMask",myMaskSmall)
    cv2.imshow("TrackingBlue",ObjectOfinterestSmall)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps = .9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()