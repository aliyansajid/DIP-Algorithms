import cv2
import numpy as np
import matplotlib.pyplot as plt

def gray_level_slicing(image_path, lower_threshold, upper_threshold):
    # Read the image
    image = cv2.imread(image_path, 0)  # Read image as grayscale

    # Apply grey level slicing
    mask = np.logical_and(image >= lower_threshold, image <= upper_threshold)
    sliced_image = image.copy()
    sliced_image[~mask] = 0  # Set pixels outside the threshold range to zero

    # Display the original and sliced images side by side
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(sliced_image, cmap='gray')
    plt.title('Sliced Image')
    plt.axis('off')

    plt.show()

# Example usage
if __name__ == "__main__":
    image_path = r'C:\Users\Aliyan Sajid\Downloads\pexels-mike-bird-170811.jpg'  # Change this to the path of your image
    lower_threshold = 100  # Lower intensity threshold
    upper_threshold = 200  # Upper intensity threshold
    gray_level_slicing(image_path, lower_threshold, upper_threshold)