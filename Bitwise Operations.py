import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and) # Basically returns the intersection of those images

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or) # Basically returns the reunion of those images


# bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor) # Basically returns the non-intersecting section from those images

# bitwise NOT
bitwise_not = cv.bitwise_not(rectangle, circle)
cv.imshow('Bitwise NOT', bitwise_not) # Basically inverted/converted from black to white, from white to black respectively
bitwise_not2 = cv.bitwise_not(circle, rectangle)
cv.imshow('Bitwise NOT2', bitwise_not2)

cv.waitKey(0)