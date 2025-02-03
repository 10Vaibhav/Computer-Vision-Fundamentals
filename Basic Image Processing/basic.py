import cv2 as cv

img = cv.imread('../Resources/Photos/boston.jpg')
cv.imshow('Boston', img)

# Converting to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
# canny = cv.Canny(blur, 125, 175) # reduce the detected edges
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Crop', cropped)
cv.waitKey(0)

# Dilation and erosion are fundamental morphological operations in image processing:

# Dilation:

# Expands or thickens objects in an image
# Adds pixels to object boundaries
# Fills small holes and gaps
# Useful for connecting broken parts of objects

# Erosion:

# Shrinks or thins objects in an image
# Removes pixels from object boundaries
# Eliminates small protrusions
# Useful for removing noise and separating connected objects

# These operations use a structuring element (kernel) that determines how the image is modified.
# They're often used together in various combinations to achieve different image processing effects.
