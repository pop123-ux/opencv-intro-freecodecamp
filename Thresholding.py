import cv2 as cv

img = cv.imread('FreeCodeCampTutorial\opencv-course\Resources\Photos\cat.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY) # 150 is the thresholded value; threshold is 150 and thresh is the image creates
cv.imshow('Thresholded Image', thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV) # 150 is the thresholded value; threshold is 150 and thresh is the image creates
cv.imshow('Thresholded Image Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)


cv.waitKey(0)