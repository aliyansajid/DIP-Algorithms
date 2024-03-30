import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(r'C:\Users\Aliyan Sajid\Downloads\pexels-mike-bird-170811.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Laplacian filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Convert the result to uint8
laplacian = np.uint8(np.absolute(laplacian))

# Display the original and filtered images side by side
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian Filtered Image')
plt.axis('off')

plt.show()