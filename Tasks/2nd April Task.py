import cv2
import numpy as np

def image_editor(image_path):
    # 1. Load the image
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not load image. Check the file path.")
        return

    # 2. Convert to Grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Apply Gaussian Blur (ksize must be odd, e.g., 7x7)
    blurred_img = cv2.GaussianBlur(img, (7, 7), 0)

    # 4. Show Edges (Canny Edge Detection)
    # We use the grayscale image for better edge results
    edges = cv2.Canny(gray_img, 100, 200)

    # Display the results
    cv2.imshow('Original', img)
    cv2.imshow('Grayscale', gray_img)
    cv2.imshow('Blurred', blurred_img)
    cv2.imshow('Edges', edges)

    print("Press any key to close the windows.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the app
image_editor('your_image.jpg') # Replace with your file name