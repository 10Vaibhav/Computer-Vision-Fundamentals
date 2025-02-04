import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
##########################################################################################################################

# GrayScale histogram
masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Mask', masked)

gray_hist = cv.calcHist([gray], [0], masked, [256], [0, 256])

plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

###############################################################################################################################
# colour Histogram
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Mask', masked)

plt.figure()
plt.title("Colour  Histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()
cv.waitKey(0)

############################################################################################################################

# OpenCV calcHist() function. Let me break down the parameters:
#
# [gray]: The source image in a list (OpenCV expects a list of images)
# [0]: The channel index (0 for grayscale)
# None: No mask is being used (entire image is considered)
# [256]: Number of bins in the histogram (typical for 8-bit images, representing 256 possible intensity values)
# [0, 256]: The range of pixel values to consider (0 to 255 inclusive)
#
# The resulting gray_hist will contain the count of pixels for each intensity level from 0 (black) to 255 (white).
# This histogram is useful for:
#
# Analyzing image intensity distribution
# Determining if an image is over/underexposed
# As a step in image processing operations like histogram equalization
