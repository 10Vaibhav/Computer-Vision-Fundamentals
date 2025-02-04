# Image Thresholding with OpenCV

This project demonstrates different image thresholding techniques using OpenCV. The script reads an image, converts it to grayscale, and applies simple and adaptive thresholding methods.

## Code Explanation

1. **Load Image:**
   ```python
   img = cv.imread('../Resources/Photos/cats.jpg')
   cv.imshow('Cats', img)
   ```
   *Reads an image and displays it.*

   ![Original Image](./Output%20Images/cats_original.jpg)

2. **Convert to Grayscale:**
   ```python
   gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
   cv.imshow('Gray', gray)
   ```
   *Converts the image to grayscale.*

   ![Grayscale Image](./Output%20Images/cats_gray.jpg)

3. **Simple Thresholding:**
   ```python
   threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
   cv.imshow('Simple Thresholding', thresh)
   ```
   *Pixels greater than 150 become white, others black.*

   ![Simple Thresholding](./Output%20Images/Simple%20Thresholding.jpg)

4. **Simple Thresholding Inverse:**
   ```python
   threshold_inv, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
   cv.imshow('Simple Thresholding Inverse', thresh_inv)
   ```
   *Inverted binary thresholding.*

   ![Simple Thresholding Inverse](./Output%20Images/Simple%20Thresholding%20Inverse.jpg)

5. **Adaptive Thresholding (Mean Method):**
   ```python
   adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
   cv.imshow('Adaptive Thresholding', adaptive_thresh)
   ```
   *Applies adaptive thresholding using the mean method.*

   ![Adaptive Thresholding](./Output%20Images/Adaptive%20Thresholding.jpg)

6. **Adaptive Thresholding (Gaussian Method):**
   ```python
   adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
   cv.imshow('Adaptive Thresholding using Gaussian', adaptive_thresh)
   ```
   *Uses Gaussian-weighted neighborhood.*

   ![Adaptive Thresholding Gaussian](./Output%20Images/Adaptive%20Thresholding%20using%20Gaussian.jpg)

7. **Adaptive Thresholding Inverse:**
   ```python
   adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
   cv.imshow('Adaptive Thresholding Inverse', adaptive_thresh_inv)
   ```
   *Inverted adaptive thresholding.*

   ![Adaptive Thresholding Inverse](./Output%20Images/Adaptive%20Thresholding%20Inverse.jpg)
