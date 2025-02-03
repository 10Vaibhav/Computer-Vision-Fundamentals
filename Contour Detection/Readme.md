# Contour Detection using OpenCV

This project demonstrates how to detect and visualize contours in an image using OpenCV. The script reads an image, processes it to detect edges, and then finds and draws contours.

## Code Explanation

### 1. Import Required Libraries
```python
import cv2 as cv
import numpy as np
```
These libraries are used for image processing (OpenCV) and numerical operations (NumPy).

### 2. Load and Display the Image
```python
img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)
```
This reads an image from the specified path and displays it in a window.

![Contours Output](./Output%20Images/Cats%20Original.png)

### 3. Convert Image to Grayscale
```python
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
```
Contours work best on grayscale images, so we convert the image to grayscale.

![Contours Output](./Output%20Images/Gray%20Cats.png)

### 4. Create a Blank Image
```python
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
```
A blank image (same size as the original) is created to draw contours later.

![Contours Output](./Output%20Images/Blank.png)

### 5. Apply Gaussian Blur
```python
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
```
Blurring helps reduce noise and improve edge detection.

![Contours Output](./Output%20Images/Blur%20cats.png)

### 6. Detect Edges using Canny Edge Detection
```python
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
```
Canny edge detection helps identify the prominent edges in the image.

![Contours Output](./Output%20Images/Canny%20Edge%20Cats.png)

### 7. Find Contours
```python
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"{len(contours)} contour's found!")
```
Contours are extracted from the edge-detected image.

### 8. Draw Contours on the Blank Image
```python
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)
```
Contours are drawn in red on the blank image for visualization.

![Contours Output](./Output%20Images/Contours.png)

### 9. Wait for a Key Press
```python
cv.waitKey(0)
```
This keeps the image windows open until a key is pressed.


## Applications of Contour Detection
- Object Detection & Recognition
- Shape Analysis
- Feature Extraction
- Motion Tracking
- Image Segmentation


### Enjoy experimenting with contour detection!

