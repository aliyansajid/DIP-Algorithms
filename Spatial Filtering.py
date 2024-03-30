import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO

# Read the image from URL
image_url = "https://images.pexels.com/photos/170811/pexels-photo-170811.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"

# Download the image
response = requests.get(image_url)
if response.status_code == 200:
    image_bytes = BytesIO(response.content)
    image = cv2.imdecode(np.frombuffer(image_bytes.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
else:
    print("Error: Unable to download the image from the URL.")

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load the image.")
else:
    # Apply Sobel filter
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Compute the gradient magnitude
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normalize the gradient magnitude to the range [0, 255]
    gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # Display the original and filtered images
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(gradient_magnitude_normalized, cmap='gray')
    plt.title('Gradient Magnitude (Sobel Filter)')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(sobel_x, cmap='gray')
    plt.title('Sobel X')
    plt.axis('off')

    plt.show()