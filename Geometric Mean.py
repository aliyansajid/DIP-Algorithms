import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

def geometric_mean_filter(image, kernel_size):
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be odd")
    padding = kernel_size // 2
    padded_image = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_CONSTANT, 0)
    filtered_image = np.zeros_like(image, dtype=np.float64)
    epsilon = 1e-8
    for y in range(padding, padded_image.shape[0] - padding):
        for x in range(padding, padded_image.shape[1] - padding):
            roi = padded_image[y - padding:y + padding + 1, x - padding:x + padding + 1]
            mean_value = np.exp(np.mean(np.log(roi + epsilon)))
            filtered_image[y - padding, x - padding] = mean_value
    return filtered_image.astype(np.uint8)

image_path = r'C:\Users\Aliyan Sajid\Desktop\soldier.jpg'

pil_image = Image.open(image_path)
image = np.array(pil_image)
if len(image.shape) > 2 and image.shape[2] == 3:
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
filtered_image = geometric_mean_filter(image, kernel_size=3)

fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')
axes[1].imshow(filtered_image, cmap='gray')
axes[1].set_title('Filtered Image')
axes[1].axis('off')
plt.show()