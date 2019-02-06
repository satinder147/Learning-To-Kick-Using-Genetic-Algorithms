import cv2
cap=cv2.VideoCapture(1)
while 1:
    frame=cap.read()[1]
    frame1=frame[140:185,40:]
    frame2=frame[190:230,40:]
    frame3=frame[230:275,40:]
    frame4=frame[275:315,80:]
    cv2.imshow("d",frame4)
    if(cv2.waitKey(1) & 0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
