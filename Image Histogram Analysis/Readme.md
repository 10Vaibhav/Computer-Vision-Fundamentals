# Image Histogram Analysis using OpenCV

## Overview
This Python script uses OpenCV and Matplotlib to compute and visualize grayscale and color histograms for an image. It also applies a circular mask to the image to analyze pixel intensity distribution within a specific region.

## Code Explanation

### 1. Import Required Libraries
```python
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
```
These libraries are used for image processing (`cv2`), numerical operations (`numpy`), and plotting (`matplotlib`).

### 2. Load and Display the Image
```python
img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)
```
Loads an image from the specified path and displays it using OpenCV.

**Output:**
![Original Image](./Output%20Images/Original%20Cats.png)

### 3. Create a Blank Mask and Convert to Grayscale
```python
blank = np.zeros(img.shape[:2], dtype="uint8")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
```
- A blank image (same dimensions as the original) is created.
- The image is converted to grayscale for histogram calculation.

**Output:**
![Grayscale Image](./Output%20Images/Gray%20Cats.png)

### 4. Apply Circular Mask
```python
mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
```
This creates a circular mask at the center of the image with a radius of 100 pixels.

![image1](./Output%20Images/Masking.png) ![image2](./Output%20Images/Colour%20Masking.png)

### 5. Compute and Display Grayscale Histogram
```python
masked = cv.bitwise_and(gray, gray, mask=mask)
gray_hist = cv.calcHist([gray], [0], masked, [256], [0, 256])
```
- The mask is applied to the grayscale image.
- `cv.calcHist()` computes the histogram for grayscale values within the masked region.

### 6. Plot the Grayscale Histogram
```python
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()
```
Displays the grayscale histogram.

**Output:**
![Grayscale Histogram](./Output%20Images/GraScale%20Historgram%20.png)

### 7. Compute and Display Color Histogram
```python
masked = cv.bitwise_and(img, img, mask=mask)
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color=col)
plt.xlim([0, 256])
plt.show()
```
- The mask is applied to the original image.
- Histograms are computed for each color channel (Blue, Green, Red) and plotted.

**Output:**
![Color Histogram](./Output%20Images/Colour%20Histogram%20.png)

### 8. Wait for Key Press to Close Windows
```python
cv.waitKey(0)
```
Prevents the script from exiting immediately so that images can be viewed.

## Output Summary
After running the script, the following will be displayed:
1. The original image
2. The grayscale image
3. The masked image
4. The grayscale histogram
5. The color histogram

### Example Output:
![Histogram Output](images/histogram_output.png)

## Conclusion
This script provides an effective way to analyze image intensity distributions, which can be useful for tasks such as:
- Image enhancement
- Thresholding
- Contrast adjustment
- Image segmentation

