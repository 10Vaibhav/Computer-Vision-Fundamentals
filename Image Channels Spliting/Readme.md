# Image Split and Merge with OpenCV

## Overview
This script demonstrates how to read, manipulate, and split image channels using OpenCV. It loads an image, separates its blue, green, and red channels, and then displays and saves each one separately.

## Code and Output
### 1. Load and Display Original Image
#### Code:
```python
import cv2 as cv
import numpy as np

# Load the image
img = cv.imread('../Resources/Photos/boston.jpg')
cv.imshow('Boston', img)
cv.imwrite("boston_original.jpg", img, [cv.IMWRITE_JPEG_QUALITY, 90])
```
#### Output:
![Original Image](./Output%20Images/boston_original.jpg)

### 2. Split Channels and Create Blank Mask
#### Code:
```python
# Create a blank mask with the same height and width as the image
blank = np.zeros(img.shape[:2], dtype="uint8")

# Split the image into its Blue, Green, and Red channels
b, g, r = cv.split(img)
```

### 3. Visualize Individual Color Channels
#### Code:
```python
# Merge individual channels with blank masks to visualize them separately
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# Display individual color channels
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)
```
#### Output:
**Blue Channel:**
![Blue Channel](./Output%20Images/blue_boston.jpg)

**Green Channel:**
![Green Channel](./Output%20Images/green_boston.jpg)

**Red Channel:**
![Red Channel](./Output%20Images/red_boston.jpg)

### 4. Merge Channels Back to Original Image
#### Code:
```python
# Merge back the channels to get the original image
merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)
```

**Merged Image:**
![Merged Channels](./Output%20Images/merged_boston.jpg)

## How it Works
1. **Reading the Image**: The image is loaded using `cv.imread()` and displayed using `cv.imshow()`.
2. **Splitting Channels**: `cv.split(img)` extracts the Blue, Green, and Red channels separately.
3. **Visualizing Channels**: Blank images are used to isolate each color component.
4. **Saving the Original Image**: The original image is saved with `cv.imwrite()`.
5. **Merging Channels**: The channels are recombined using `cv.merge([b, g, r])` to reconstruct the original image.

