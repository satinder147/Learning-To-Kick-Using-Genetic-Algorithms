import cv2
cap=cv2.VideoCapture(0)
while 1:
    frame=cap.read()[1]
    frame1=frame[135:210,:]
    frame2=frame[207:278,:]
    frame3=frame[278:360,:]
    frame4=frame[360:430,:]
    cv2.imshow("d",frame)
    cv2.imshow("sl",frame4)
    if(cv2.waitKey(1) & 0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
