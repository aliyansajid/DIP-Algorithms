import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_stretching(image):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    min_val = np.min(image)
    max_val = np.max(image)
    stretched_image = (image - min_val) * (255.0 / (max_val - min_val))
    stretched_image = stretched_image.astype(np.uint8)
    return stretched_image

image_path = 'C:/Users/Aliyan Sajid/Desktop/soldier.jpg'

image = cv2.imread(image_path)
stretched_image = histogram_stretching(image)

hist_original, bins_original = np.histogram(image.flatten(), 256, [0, 256])
hist_stretched, bins_stretched = np.histogram(stretched_image.flatten(), 256, [0, 256])
cdf_original = hist_original.cumsum()
cdf_stretched = hist_stretched.cumsum()
cdf_original_normalized = cdf_original / cdf_original.max()
cdf_stretched_normalized = cdf_stretched / cdf_stretched.max()

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

axs[0, 1].imshow(stretched_image, cmap='gray')
axs[0, 1].set_title('Stretched Image')
axs[0, 1].axis('off')

axs[1, 0].plot(cdf_original_normalized, color='b')
axs[1, 0].hist(image.flatten(), 256, [0, 256], color='r')
axs[1, 0].set_title('Original Histogram')
axs[1, 0].set_xlabel('Pixel Intensity')
axs[1, 0].set_ylabel('Frequency')

axs[1, 1].plot(cdf_stretched_normalized, color='b')
axs[1, 1].hist(stretched_image.flatten(), 256, [0, 256], color='r')
axs[1, 1].set_title('Stretched Histogram')
axs[1, 1].set_xlabel('Pixel Intensity')
axs[1, 1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()