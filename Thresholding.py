import cv2
import numpy as np
import matplotlib.pyplot as plt

def threshold_image(image_path, threshold_value):
    # Read the image
    image = cv2.imread(image_path, 0)  # Read image as grayscale

    # Apply thresholding
    _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

    # Display the original and thresholded images side by side
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(thresholded_image, cmap='gray')
    plt.title('Thresholded Image')
    plt.axis('off')

    plt.show()

# Example usage
if __name__ == "__main__":
    image_path = r'C:\Users\Aliyan Sajid\Downloads\pexels-mike-bird-170811.jpg'  # Change this to the path of your image
    threshold_value = 127  # Change this threshold value as required
    threshold_image(image_path, threshold_value)
