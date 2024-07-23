import cv2
from picamera2 import Picamera2
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
while True:
    tStart=time.time()
    frame=piCam.capture_array()
    ROI=frame[:int(disph/2),:int(dispw/2)]
    #frame[:int(disph/2),:int(dispw/2)]=[0,0,255]
    #frame[:int(disph/2),int(dispw/2):]=[255,0,0]
    #frame[int(disph/2):,int(dispw/2):]=[0,255,0]
    #frame[int(disph/2):,:int(dispw/2)]=[0,125,125]
    
    frame[:int(disph/2),int(dispw/2):] = ROI
    frame[int(disph/2):,int(dispw/2):] = ROI
    frame[int(disph/2):,:int(dispw/2)] = ROI
    cv2.putText(frame,str(int(fps)),pos,font,height,myColor,weight)
    #cv2.imshow("piCam",frame)
    cv2.imshow("ROI",ROI)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps = .9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()