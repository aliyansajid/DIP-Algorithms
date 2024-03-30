import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image_path, gamma):
    # Read the image
    image = cv2.imread(image_path, 0)  # Read image as grayscale

    # Perform gamma correction
    gamma_corrected_image = np.uint8(((image / 255.0) ** gamma) * 255)

    # Display the original and gamma-corrected images side by side
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(gamma_corrected_image, cmap='gray')
    plt.title('Gamma Corrected Image (Gamma={})'.format(gamma))
    plt.axis('off')

    plt.show()

# Example usage
if __name__ == "__main__":
    image_path = r'C:\Users\Aliyan Sajid\Downloads\pexels-mike-bird-170811.jpg'  # Change this to the path of your image
    gamma = 1.5  # Gamma value, adjust as needed
    gamma_correction(image_path, gamma)