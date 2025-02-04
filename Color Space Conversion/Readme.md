# Color Space Conversion using OpenCV

## Overview
This script demonstrates color space conversions using OpenCV. It loads an image, converts it into different color spaces, and displays the results. The converted images are also shown using Matplotlib.


## Code Explanation

1. **Read and Display the Original Image**
   ```python
   img = cv.imread('../Resources/Photos/boston.jpg')
   cv.imshow('Boston', img)
   ```
   *Reads the image from the specified path and displays it.*
   
   ![Original Image](./Output%20Images/Boston_original.jpg)

2. **Convert to Grayscale**
   ```python
   gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
   cv.imshow('Gray', gray)
   ```
   *Converts the image to grayscale.*
   
   ![Grayscale Image](./Output%20Images/gray.jpg)

3. **Convert to HSV (Hue, Saturation, Value)**
   ```python
   hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
   cv.imshow('HSV', hsv)
   ```
   *Converts the image to HSV color space.*
   
   ![HSV Image](./Output%20Images/hsv.jpg)

4. **Convert to LAB (L*a*b)**
   ```python
   lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
   cv.imshow('LAB', lab)
   ```
   *Converts the image to LAB color space.*
   
   ![LAB Image](./Output%20Images/lab.jpg)

5. **Convert to RGB**
   ```python
   rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
   cv.imshow('RGB', rgb)
   ```
   *Converts the image to RGB color space.*
   
   ![RGB Image](./Output%20Images/rgb.jpg)

6. **Convert Back to BGR from HSV and LAB**
   ```python
   hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
   lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
   cv.imshow('HSV ---> BGR', hsv_bgr)
   cv.imshow('LAB ---> BGR', lab_bgr)
   ```
   *Converts HSV and LAB images back to BGR.*
   
   ![HSV to BGR](./Output%20Images/hav_bgr.jpg)
   ![LAB to BGR](./Output%20Images/lab_bgr.jpg)


