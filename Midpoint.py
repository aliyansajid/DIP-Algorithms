import numpy as np
import cv2
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
def midpoint_filter(image, kernel_size):
    if kernel_size % 2 == 0:
        raise ValueError("Kernel size must be odd")
    padding = kernel_size // 2
    padded_image = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_CONSTANT, 0)
    filtered_image = np.zeros_like(image)
    for y in range(padding, padded_image.shape[0] - padding):
        for x in range(padding, padded_image.shape[1] - padding):
            roi = padded_image[y - padding:y + padding + 1, x - padding:x + padding + 1]
            midpoint_value = (np.max(roi) + np.min(roi)) / 2
            filtered_image[y - padding, x - padding] = midpoint_value
    return filtered_image
image_url = 'https://images.pexels.com/photos/210019/pexels-photo-210019.jpeg?cs=srgb&dl=pexels-pixabay-210019.jpg&fm=jpg'
response = requests.get(image_url)
if response.status_code == 200:
    pil_image = Image.open(BytesIO(response.content))
    image = np.array(pil_image)
    if len(image.shape) > 2 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    filtered_image = midpoint_filter(image, kernel_size=3)
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    axes[1].imshow(filtered_image, cmap='gray')
    axes[1].set_title('Filtered Image')
    axes[1].axis('off')
    plt.show()
else:    print("Error: Unable to download image from URL.")