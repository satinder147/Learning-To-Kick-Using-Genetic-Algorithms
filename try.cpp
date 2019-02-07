import cv2
cap=cv2.VideoCapture(1)
while 1:
  ret,frame=cap.read()
  cv2.imshow("s",frame)
  cv2.waitKey(1)
cv2.destroyAllWindows()
cap.release()
