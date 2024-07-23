import cv2
from picamera2 import Picamera2
import time
piCam=Picamera2()
def TrackX(val):
    global xpos
    xpos = val
def TrackY(val):
    global ypos
    ypos = val
def TrackW(val):
    global boxw
    boxw = val
def TrackH(val):
    global boxh
    boxh = val
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
cv2.createTrackbar('X Pos','My Trackbars',10,dispw-1,TrackX)
cv2.createTrackbar('Y Pos','My Trackbars',10,disph-1,TrackY)
cv2.createTrackbar('Box Width','My Trackbars',10,dispw-1,TrackW)
cv2.createTrackbar('Box Height','My Trackbars',10,disph-1,TrackH)
while True:
    tStart=time.time()
    frame=piCam.capture_array()
    ROI=frame[ypos:ypos+boxh,xpos:xpos+boxw]
    cv2.putText(frame,str(int(fps)),pos,font,height,myColor,weight)
    cv2.rectangle(frame,(xpos,ypos),(xpos+boxw,ypos+boxh),myColor,weight)
    cv2.imshow("piCam",frame)
    cv2.imshow("ROI",ROI)
    if cv2.waitKey(1)==ord('q'):
        break
    tEnd=time.time()
    loopTime=tEnd-tStart
    fps = .9*fps + .1*(1/loopTime)
cv2.destroyAllWindows()