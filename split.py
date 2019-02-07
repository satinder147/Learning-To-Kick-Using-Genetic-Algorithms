import cv2
cap=cv2.VideoCapture(1)
while 1:
    frame=cap.read()[1]
    frame1=frame[30:120,:]
    frame2=frame[125:200,:]
    frame3=frame[210:270,:]
    frame4=frame[285:370,:]
    cv2.imshow("d",frame)
    cv2.imshow("sl",frame3)
    if(cv2.waitKey(1) & 0XFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
