import cv2 as cv

img = cv.imread('FreeCodeCampTutorial\opencv-course\Resources\Photos\cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gaussian)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur
bilat = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilat)

cv.waitKey(0)