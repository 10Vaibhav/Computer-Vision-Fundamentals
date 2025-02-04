import cv2 as cv

# Reading Images
img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Interpolation is a method of estimating unknown values between known data points.
# In image processing, it's used to:

# Resize images (scaling up/down)
# Rotate images
# Correct geometric distortions

# Common interpolation methods:
# Nearest neighbor: Uses closest pixel value
# Linear: Weighted average of two points
# Bilinear: Linear interpolation in 2D
# Bicubic: Uses 16 neighboring pixels for smoother results
# Spline: Uses polynomial functions for smooth curves

# Each method offers different trade-offs between quality and computational cost.


resized_image = rescaleFrame(img)

cv.imshow('Image', resized_image)


def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)


# Reading Videos
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# cv.waitKey(0)
