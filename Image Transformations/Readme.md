# Image Transformations using OpenCV

## Overview
This project demonstrates various image processing techniques using OpenCV, such as translation, rotation, resizing, flipping, and cropping.

## Code Explanation

### 1. **Loading the Image**
```python
img = cv.imread('../Resources/Photos/boston.jpg')
cv.imshow("Boston", img)
```
This loads an image named `boston.jpg` from the specified path and displays it.

![Output](./Output%20Images/boston.png)

### 2. **Translation**
Translation moves an image in the x or y direction.
```python
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)
```
- **x**: Moves the image right (+) or left (-)
- **y**: Moves the image down (+) or up (-)

![Output](./Output%20Images/Translated.png)

### 3. **Rotation**
Rotates the image by a given angle around a specified point.
```python
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)
rotated_rotated = rotate(rotated, -45)
cv.imshow("Rotate Rotated", rotated_rotated)
```

![Output](./Output%20Images/Rotated.png)
- Rotates the image by -45 degrees.

![Output](./Output%20Images/Rotate%20Rotated.png)
- Rotates the already rotated image by another -45 degrees.

### 4. **Resizing**
Resizes the image to 500x500 pixels using cubic interpolation.
```python
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)
```

![Output](./Output%20Images/Resized.png)

### 5. **Flipping**
Flips the image in different directions.
```python
flip = cv.flip(img, -1)  # Flip both vertically and horizontally
cv.imshow("Flip", flip)
```
- `0`: Vertical flip
- `1`: Horizontal flip
- `-1`: Both vertical and horizontal flip

![Output](./Output%20Images/Flip.png)

### 6. **Cropping**
Extracts a region from the image.
```python
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)
```
Crops the region from row 200 to 400 and column 300 to 400.

![Output](./Output%20Images/cropping.png)





