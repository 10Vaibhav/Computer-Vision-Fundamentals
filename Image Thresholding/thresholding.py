import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)
# cv.imwrite("cats_original.jpg", img, [cv.IMWRITE_JPEG_QUALITY, 90])

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
# cv.imwrite("cats_gray.jpg", gray, [cv.IMWRITE_JPEG_QUALITY, 90])

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholding', thresh)
# cv.imwrite("Simple Thresholding.jpg", thresh, [cv.IMWRITE_JPEG_QUALITY, 90])

# Simple Thresholding Inverse
threshold_inv, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholding Inverse', thresh_inv)
# cv.imwrite("Simple Thresholding Inverse.jpg", threshold_inv, [cv.IMWRITE_JPEG_QUALITY, 90])

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)
# cv.imwrite("Adaptive Thresholding.jpg", adaptive_thresh, [cv.IMWRITE_JPEG_QUALITY, 90])

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding using Gaussian', adaptive_thresh)
# cv.imwrite("Adaptive Thresholding using Gaussian.jpg", adaptive_thresh, [cv.IMWRITE_JPEG_QUALITY, 90])

# Adaptive Thresholding Inverse
adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Thresholding Inverse', adaptive_thresh_inv)
# cv.imwrite("Adaptive Thresholding Inverse.jpg", adaptive_thresh_inv, [cv.IMWRITE_JPEG_QUALITY, 90])

cv.waitKey(0)

