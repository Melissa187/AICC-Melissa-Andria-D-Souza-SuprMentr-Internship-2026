#Assignment (06/04/2026)

#Assignment Name : Image as Numbers
#Description : Load an image, print shape, pixel values, channels, and explain them.

import cv2

# 1. Load the image
# Replace 'image.jpg' with any image file in your folder
img = cv2.imread('your_image.jpg')

# 2. Print Shape
# Returns (Height, Width, Number of Channels)
shape = img.shape
print(f"Image Shape: {shape}")

# 3. Print Channels
channels = shape[2] if len(shape) > 2 else 1
print(f"Number of Channels: {channels}")

# 4. Access Pixel Values
# Let's look at the pixel at row 100, column 100
pixel_value = img[100, 100]
print(f"Pixel value at (100, 100): {pixel_value}")

# 5. Total Number of Pixels
print(f"Total Pixels: {img.size}")