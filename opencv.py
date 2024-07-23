import cv2
from picamera2 import Picamera2
import time
piCam=Picamera2()
piCam.preview_configuration.main.size=(1280,720)
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
a=350
b=125
c=250
d=50
r=2
p=2
rcolor=(255,255,255)
thikness=-1
while True:
    tStart=time.time()
    frame=piCam.capture_array()
    #print(frame[0,0])
    cv2.putText(frame,str(int(fps)),pos,font,height,myColor,weight)
    upperleft=(c,d)
    lowerright=(a,b)
    cv2.rectangle(frame,upperleft,lowerright,rcolor,thikness)
    c += r
    a += r
    d += p
    b += p
    if a >= 1279:
        r = -2
    elif b >= 719:
        p = -2
    elif c <= 0:
        r = 2
    elif d <= 0:
        p = 2
    cv2.imshow("piCam",frame)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps = .9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()