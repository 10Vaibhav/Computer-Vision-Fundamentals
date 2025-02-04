# Image Smoothing using OpenCV

## Description
This Python script demonstrates different image smoothing techniques using OpenCV:

- **Averaging Blur**
- **Gaussian Blur**
- **Median Blur**
- **Bilateral Filtering**

Each technique is applied to an input image, and the results are displayed using OpenCV's `imshow` function.

## Prerequisites
Before running the script, ensure you have OpenCV installed:
```sh
pip install opencv-python
```

## Code and Output

### 1. Original Image
```python
import cv2 as cv

# Load Image
img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)
```
**Output:**

![Original Image](./Output%20Images/cats_original.jpg)

---

### 2. Averaging Blur
```python
# Averaging Blur
average = cv.blur(img, (3, 3))
cv.imshow('Average Blur', average)
```
**Output:**

![Averaging Blur](./Output%20Images/Average_Blur.jpg)

---

### 3. Gaussian Blur
```python
# Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)
```
**Output:**

![Gaussian Blur](./Output%20Images/Gaussian_Blur.jpg)

---

### 4. Median Blur
```python
# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)
```
**Output:**

![Median Blur](./Output%20Images/Median_Blur.jpg)

---

### 5. Bilateral Filtering
```python
# Bilateral Filtering
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow('Bilateral', bilateral)
```
**Output:**

![Bilateral Filtering](./Output%20Images/Bilateral_Blur.jpg)
