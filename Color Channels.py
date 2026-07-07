import cv2 as cv
import numpy as np

img = cv.imread('FreeCodeCampTutorial\opencv-course\Resources\Photos\lady.jpg')
cv.imshow('Lady', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img) # Show the distribution of pixel intensities

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# Grayscale images have a shape of 1
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)