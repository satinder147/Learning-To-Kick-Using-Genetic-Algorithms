import cv2
import numpy as np

lowero=np.array([0,136,126])
uppero=np.array([20,255,255])

lowerb=np.array([90,65,82])
upperb=np.array([116,255,255])

lowerg=np.array([45,48,157])
upperg=np.array([55,255,255])

def getCenter(frame,lower,upper):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower,upper)
    mask=cv2.dilate(mask,None,iterations=2)
    mask=cv2.erode(mask,None,iterations=2)
    _,contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if(len(contours)!=0):
        #cv2.drawContours(frame,contours,-1,(255,0,0),2)
        c=max(contours,key=cv2.contourArea)
        x,y,w,h=cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        center=[]
        center.append((x+w)/2)
        center.append((y+h)/2)
    return frame,center

cap=cv2.VideoCapture(1)

while True:
    ret,frame=cap.read()
    frame,centero=getCenter(frame,lowero,uppero)
    frame,centerb=getCenter(frame,lowerb,upperb)
    frame,centerg=getCenter(frame,lowerg,upperg)
    
    cv2.imshow("d",frame)
    if(cv2.waitKey(1) & 0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
