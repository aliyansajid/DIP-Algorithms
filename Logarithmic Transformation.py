import cv2
import numpy as np
import matplotlib.pyplot as plt

def log_transform(image_path, c):
    # Read the image
    image = cv2.imread(image_path, 0)  # Read image as grayscale

    # Perform logarithmic transformation
    log_transformed_image = c * np.log1p(image)

    # Normalize the image to 0-255 range
    log_transformed_image = ((log_transformed_image - log_transformed_image.min()) * (255 / (log_transformed_image.max() - log_transformed_image.min()))).astype(np.uint8)

    # Display the original and transformed images side by side
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(log_transformed_image, cmap='gray')
    plt.title('Logarithmic Transformed Image')
    plt.axis('off')

    plt.show()

# Example usage
if __name__ == "__main__":
    image_path = r'C:\Users\Aliyan Sajid\Downloads\pexels-mike-bird-170811.jpg'  # Change this to the path of your image
    c = 0.1  # Constant for logarithmic transformation, adjust as needed
    log_transform(image_path, c)