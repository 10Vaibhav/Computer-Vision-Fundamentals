# Image Processing with OpenCV

## Overview
This script performs various image processing operations using OpenCV. It reads an image, applies transformations like grayscale conversion, blurring, edge detection, dilation, erosion, resizing, and cropping. The results are displayed in separate windows.


## Code Explanation

1. **Reading and Displaying the Image**
    ```python
    img = cv.imread('../Resources/Photos/boston.jpg')
    cv.imshow('Boston', img)
    ```
    - Reads the image from the specified path and displays it.

    ![Original Image](./Output%20Images/boston.jpg)

2. **Converting to Grayscale**
    ```python
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)
    ```
    - Converts the image from BGR to grayscale.

    ![Grayscale Image](./Output%20Images/GrayScale%20.png)

3. **Applying Gaussian Blur**
    ```python
    blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
    cv.imshow('Blur', blur)
    ```
    - Blurs the image using a 7x7 kernel to reduce noise.

    ![Blurred Image](./Output%20Images/Blur.png)

4. **Edge Detection (Canny)**
    ```python
    canny = cv.Canny(img, 125, 175)
    cv.imshow('Canny Edges', canny)
    ```
    - Detects edges in the image using the Canny edge detection algorithm.

    ![Edge Detection](./Output%20Images/Canny%20Edge%20Detection.png)

5. **Dilating the Edges**
    ```python
    dilated = cv.dilate(canny, (3, 3), iterations=1)
    cv.imshow("Dilated", dilated)
    ```
    - Expands the edges detected by the Canny algorithm.

    ![Dilated Image](./Output%20Images/Dilated.png)

6. **Eroding the Image**
    ```python
    eroded = cv.erode(dilated, (3, 3), iterations=1)
    cv.imshow('Eroded', eroded)
    ```
    - Shrinks the dilated edges, restoring some original shapes.

    ![Eroded Image](./Output%20Images/Eroded.png)

7. **Resizing the Image**
    ```python
    resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
    cv.imshow('Resized', resized)
    ```
    - Resizes the image to 500x500 pixels.

    ![Resized Image](./Output%20Images/Resized.png)

8. **Cropping the Image**
    ```python
    cropped = img[50:200, 200:400]
    cv.imshow('Crop', cropped)
    ```
    - Extracts a region from the original image.

    ![Cropped Image](./Output%20Images/Crop.png)


## Conclusion
This script demonstrates fundamental image processing techniques using OpenCV. You can experiment with different parameters to observe varying effects on the images.

