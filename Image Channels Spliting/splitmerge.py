import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/boston.jpg')
cv.imshow('Boston', img)
cv.imwrite("boston_original.jpg", img, [cv.IMWRITE_JPEG_QUALITY, 90])

blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
