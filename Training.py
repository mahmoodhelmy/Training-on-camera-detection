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
    thresh = cv2.threshold(dif,60,255,cv2.THRESH_BINARY)[1]
    filter= cv2.dilate (thresh,None,iterations=2)

    cv2.imshow("vid",filter)

    contours , check = cv2.findContours(filter,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for con in contours:
        if cv2.contourArea(con) <5000:
            continue
        x,y,w,h=cv2.boundingRect(con)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0))



    cv2.imshow("video",frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key  == ord("s"):
        cv2.imwrite("new2.jpg",frame)
vid.release()