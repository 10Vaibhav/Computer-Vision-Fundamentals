# OpenCV Drawing Example

## Description
This Python script uses OpenCV (`cv2`) to create and modify an image by drawing various shapes and adding text. The script demonstrates basic image processing techniques such as:

1. Creating a blank image.
2. Coloring the image.
3. Drawing shapes (rectangle, circle, and line).
4. Adding text to the image.

---

## Code Explanation

### 1. Import Libraries
```python
import cv2 as cv
import numpy as np
```
- `cv2` is OpenCV, a library for image processing.
- `numpy` is used to create and manipulate the image array.

### 2. Creating a Blank Image
```python
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)
```
- Creates a 500x500 pixel image with three color channels (RGB), initialized to black.
- Displays the blank image.

![Output Image](./Output%20Images/Blank.png)

### 3. Painting the Image
```python
blank[:] = 0, 255, 0  # Green
blank[:] = 0, 0, 255  # Red
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('Red', blank)
```
- Changes the entire image to red.
- Colors a specific region (200:300 height, 300:400 width) in red.

![Output Image](./Output%20Images/Red.png)

### 4. Drawing a Rectangle
```python
cv.rectangle(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)
```
- Draws a green rectangle from the top-left corner to the center.

![Output Image](./Output%20Images/Draw%20Rectangle.png)

### 5. Drawing a Circle
```python
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (255, 0, 0), thickness=-1)
cv.imshow('Circle', blank)
```
- Draws a blue filled circle at the center of the image with a radius of 40 pixels.

![Output Image](./Output%20Images/Circle.png)

### 6. Drawing a Line
```python
cv.line(blank, (100, 250), (300, 400), (255, 255, 255), thickness=3)
cv.imshow('Line', blank)
```
- Draws a white line from point (100,250) to (300,400).

![Output Image](./Output%20Images/Line.png)

### 7. Adding Text
```python
cv.putText(blank, 'Hello, My Name is Vaibhav!!', (10, 450), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)
```
- Adds green text at the bottom-left corner.

![Output Image](./Output%20Images/Text.png)

### 8. Displaying the Image
```python
cv.waitKey(0)
```
- Keeps the displayed images open until a key is pressed.

---


