import cv2
import numpy as np
import matplotlib.pyplot as plt

def min_filter(image, kernel_size):
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be odd")
    return cv2.erode(image, np.ones((kernel_size, kernel_size), np.uint8), iterations=1)

def max_filter(image, kernel_size):
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be odd")
    return cv2.dilate(image, np.ones((kernel_size, kernel_size), np.uint8), iterations=1)

image_path = r'C:\Users\Aliyan Sajid\Desktop\soldier.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
min_filtered_image = min_filter(image, kernel_size=3)
max_filtered_image = max_filter(image, kernel_size=3)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(min_filtered_image, cmap='gray')
axes[1].set_title('Min Filtered Image')
axes[1].axis('off')
axes[2].imshow(max_filtered_image, cmap='gray')
axes[2].set_title('Max Filtered Image')
axes[2].axis('off')
plt.show()