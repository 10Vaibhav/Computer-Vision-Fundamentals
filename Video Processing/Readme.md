# OpenCV Video Processing

## Overview
This script demonstrates how to use OpenCV (`cv2`) to read and display a video file frame by frame. It also includes commented-out code for reading and displaying an image.

## Prerequisites
Ensure you have OpenCV installed in your Python environment:
```bash
pip install opencv-python
```

## Code Explanation

### Importing OpenCV
```python
import cv2 as cv
```
This imports the OpenCV library and assigns it an alias `cv`.

### Reading an Image (Commented Out)
```python
# img = cv.imread("../Resources/Photos/cat_large.jpg")
# cv.imshow('Cat', img)
# cv.waitKey(0)
```
- The script reads an image file using `cv.imread()`.
- Displays the image in a window using `cv.imshow()`.
- `cv.waitKey(0)` waits indefinitely until a key is pressed before closing the window.

### Reading and Displaying a Video
```python
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')
```
- `cv.VideoCapture()` loads the video file located at `../Resources/Videos/dog.mp4`.
- If a webcam stream is desired, change the argument to `0` (default webcam) instead of a file path.

### Looping Through Video Frames
```python
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
```
- `capture.read()` reads each frame from the video.
- `isTrue` is `True` when frames are successfully read.
- `cv.imshow('Video', frame)` displays the frame.

### Stopping the Video on Key Press
```python
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
```
- The loop continues until the user presses the 'd' key.
- `cv.waitKey(20)` waits 20 milliseconds before moving to the next frame.

### Releasing Resources
```python
capture.release()
cv.destroyAllWindows()
```
- `capture.release()` releases the video resource.
- `cv.destroyAllWindows()` closes all OpenCV windows.

## Video Output
[!Watch the video](./Video/dog.mp4)


## Summary
- The script reads and displays a video file using OpenCV.
- The loop continues until the 'd' key is pressed.
- Resources are released at the end to prevent memory issues.


# Rescaling Videos

## Description
This script demonstrates how to use OpenCV to:
- Read and display images.
- Resize images using interpolation.
- Read and resize videos.


## Code Explanation

### 1. Reading and Displaying an Image
```python
img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Cat', img)
```
This loads an image (`cat.jpg`) and displays it using OpenCV's `imshow()` function.

### 2. Rescaling Images and Videos
The `rescaleFrame()` function rescales an image, video, or live video frame by a given scale factor (default: 0.75).
```python
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
```

### 3. Resizing an Image
```python
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)
```
This rescales the loaded image and displays the resized version.

### 4. Reading and Resizing a Video
```python
capture = cv.VideoCapture('../Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
```
- This reads a video (`dog.mp4`) and displays both the original and resized versions.
- The loop continues reading frames until the user presses the `d` key.

### 5. Changing Resolution for Live Video
```python
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
```
This function sets the resolution for live video capture (webcam input).

### 6. Releasing Resources
```python
capture.release()
cv.destroyAllWindows()
```
Releases the video capture object and closes all OpenCV windows.



