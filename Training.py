import cv2

import time
vid = cv2.VideoCapture(0)
first =None
time.sleep(1)
while True:
    check , frame = vid.read()
    gre =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gau = cv2.GaussianBlur(gre,(21,21),0)

    if first is None:
        first= gau
    dif=cv2.absdiff(first,gau)    
    cv2.imshow("vid",dif)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key  == ord("s"):
        cv2.imwrite("new2.jpg",frame)
vid.release()