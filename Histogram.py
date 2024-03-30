import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_to_histogram(image_path):
    # Read the image
    img = cv2.imread(image_path)  # Read the image

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculate histogram
    hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])

    # Plot the original image
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    # Plot the histogram
    plt.subplot(1, 2, 2)
    plt.hist(gray_img.ravel(), 256, [0, 256])
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.title('Histogram')

    plt.show()

# Use raw string literal
image_to_histogram(r'C:\Users\Aliyan Sajid\Downloads\pexels-mike-bird-170811.jpg')