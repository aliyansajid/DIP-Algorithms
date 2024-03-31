import numpy as np
import cv2
import matplotlib.pyplot as plt

def median_filter(image, kernel_size):
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be odd")
    padding = kernel_size // 2
    padded_image = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_CONSTANT, 0)
    filtered_image = np.zeros_like(image)
    for y in range(padding, padded_image.shape[0] - padding):
        for x in range(padding, padded_image.shape[1] - padding):
            roi = padded_image[y - padding:y + padding + 1, x - padding:x + padding + 1]
            median_value = np.median(roi)
            filtered_image[y - padding, x - padding] = median_value
    return filtered_image

image_path = r'C:\Users\Aliyan Sajid\Desktop\soldier.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
filtered_image = median_filter(image, kernel_size=3)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title('Filtered Image')
axes[1].axis('off')
plt.show()