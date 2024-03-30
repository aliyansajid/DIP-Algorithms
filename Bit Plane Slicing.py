import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slicing(image_path):
    # Read the image
    image = cv2.imread(image_path, 0)  # Read image as grayscale

    # Get the bit planes
    bit_planes = [np.bitwise_and(image, 2**i) for i in range(8)]

    # Display the original image and its bit planes
    plt.figure(figsize=(12, 8))
    plt.subplot(3, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    for i in range(1, 9):
        plt.subplot(3, 3, i+1)
        plt.imshow(bit_planes[i-1], cmap='gray')
        plt.title('Bit Plane ' + str(i-1))
        plt.axis('off')

    plt.show()

# Example usage
if __name__ == "__main__":
    image_path = r'C:\Users\Aliyan Sajid\Downloads\pexels-mike-bird-170811.jpg'  # Change this to the path of your image
    bit_plane_slicing(image_path)
