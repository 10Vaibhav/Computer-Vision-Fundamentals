import cv2 as cv

img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)
# cv.imwrite("cats_original.jpg", img, [cv.IMWRITE_JPEG_QUALITY, 90])

# Averaging
average = cv.blur(img, (3, 3))
cv.imshow('Average Blur', average)
# cv.imwrite("Average_Blur.jpg", average, [cv.IMWRITE_JPEG_QUALITY, 90])

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)
# cv.imwrite("Gaussian_Blur.jpg", gauss, [cv.IMWRITE_JPEG_QUALITY, 90])

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)
# cv.imwrite("Median_Blur.jpg", median, [cv.IMWRITE_JPEG_QUALITY, 90])

# Bilateral Blurring
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('Bilateral', bilateral)
# cv.imwrite("Bilateral_Blur.jpg", bilateral, [cv.IMWRITE_JPEG_QUALITY, 90])

cv.waitKey(0)
