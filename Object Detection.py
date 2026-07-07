import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow("Trackbars")

cv.createTrackbar("L-H","Trackbars",0,179,nothing)
cv.createTrackbar("L-S","Trackbars",0,255,nothing)
cv.createTrackbar("L-V","Trackbars",0,255,nothing)

cv.createTrackbar("U-H","Trackbars",179,179,nothing)
cv.createTrackbar("U-S","Trackbars",255,255,nothing)
cv.createTrackbar("U-V","Trackbars",255,255,nothing)

cap = cv.VideoCapture(0)

while(cap.isOpened()):

    ret, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("L-H","Trackbars")
    l_s = cv.getTrackbarPos("L-S","Trackbars")
    l_v = cv.getTrackbarPos("L-V","Trackbars")

    u_h = cv.getTrackbarPos("U-H","Trackbars")
    u_s = cv.getTrackbarPos("U-S","Trackbars")
    u_v = cv.getTrackbarPos("U-V","Trackbars")

    lower_blue = np.array([l_h,l_s,l_v])
    upper_blue = np.array([u_h,u_s,u_v])

    mask = cv.inRange(hsv, lower_blue, upper_blue)

    mask = cv.erode(mask, None, iterations=1)
    mask = cv.dilate(mask, None, iterations=2)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)

    k = cv.waitKey(5) & 0xFF

    if k == 27:
        break

cv.destroyAllWindows()
cap.release()