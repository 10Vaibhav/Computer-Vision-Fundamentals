# Image Masking with OpenCV

## Overview
This script demonstrates how to use image masking techniques in OpenCV. The script:
1. Reads an image.
2. Creates a blank mask.
3. Generates a circular and a rectangular mask.
4. Combines the two masks using bitwise operations.
5. Applies the custom mask to the image.
6. Displays the original image, masks, and the final masked image.

## Code Explanation

### 1. Import Libraries
```python
import cv2 as cv
import numpy as np
```
OpenCV (`cv2`) is used for image processing, and NumPy (`np`) is used to handle arrays.

### 2. Load Image
```python
img = cv.imread("../Resources/Photos/cats 2.jpg")
cv.imshow('Cats', img)
```
The script loads an image and displays it.

**Original Image:**
![Original Image](./Output%20Images/Cats.png)

### 3. Create a Blank Mask
```python
blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank Image", blank)
```
A blank image of the same size as the input image is created.

**Blank Mask:**
![Blank Mask](./Output%20Images/Blank.png)

### 4. Create a Circular Mask
```python
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
cv.imshow('Mask', circle)
```
A circle mask is drawn in the center of the image.

**Circular Mask:**
![Circular Mask](./Output%20Images/Circle%20Mask.png)

### 5. Create a Rectangular Mask
```python
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
```
A rectangle mask is created.

**Rectangular Mask:**
![Rectangular Mask](./Output%20Images/Rectangular%20Mask.png)

### 6. Combine Shapes with Bitwise AND
```python
weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird shape', weird_shape)
```
The circle and rectangle masks are combined using the `bitwise_and` operation.

**Combined Mask:**
![Combined Mask](./Output%20Images/Weired%20Shape.png)

### 7. Apply Mask to Image
```python
masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)
```
The custom mask is applied to the image.

### 8. Display the Result
```python
cv.waitKey(0)
```
The images remain displayed until a key is pressed.

## Output
The script produces the following output:

**Final Masked Image:**
![Masked Output](./Output%20Images/Wired%20Shaped%20Mask.png)



