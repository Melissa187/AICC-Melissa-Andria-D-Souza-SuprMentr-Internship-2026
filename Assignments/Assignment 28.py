#Assignment (08/04/2026)

#Assignment Name : Image Filter Lab
#Description : Use OpenCV to grayscale, blur, detect edges and show before/after.
import cv2
import numpy as np

# 1. Load the original image
image = cv2.imread('your_image.jpg')

# 2. Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Apply Gaussian Blur (5x5 kernel)
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# 4. Edge Detection (Canny)
# We use the grayscale image for better edge results
edges = cv2.Canny(gray_image, 100, 200)

# 5. Display the results
cv2.imshow('Original', image)
cv2.imshow('Grayscale', gray_image)
cv2.imshow('Blurred', blurred_image)
cv2.imshow('Edge Detection', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()