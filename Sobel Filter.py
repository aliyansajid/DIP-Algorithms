import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(r'C:\Users\Aliyan Sajid\Downloads\pexels-mike-bird-170811.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Sobel filter
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Combine the x and y gradient magnitudes
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Convert the result to uint8
sobel_combined = np.uint8(sobel_combined)

# Display the original and Sobel filtered images side by side
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(sobel_combined, cmap='gray')
plt.title('Sobel Filtered Image')
plt.axis('off')

plt.show()