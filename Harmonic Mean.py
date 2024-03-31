import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def harmonic_mean_filter(image, window_size):
    image_float = image.astype(np.float32)
    reciprocal_image = np.where(image_float != 0, 1.0 / image_float, 0)
    kernel = np.ones((window_size, window_size), np.float32)
    filtered_image = cv2.filter2D(reciprocal_image, -1, kernel)
    harmonic_mean_image = np.where(filtered_image != 0, 1.0 / filtered_image, 0)
    harmonic_mean_image = (harmonic_mean_image * 255).astype(np.uint8)
    return harmonic_mean_image

image_path = r'C:\Users\Aliyan Sajid\Desktop\soldier.jpg'
image = np.array(Image.open(image_path))
window_size = 5

filtered_image = harmonic_mean_filter(image, window_size)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(filtered_image)
plt.title('Filtered Image')
plt.axis('off')
plt.show()