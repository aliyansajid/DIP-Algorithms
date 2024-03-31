import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_sliding(image):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = ((cdf - cdf.min()) * 255) / (cdf.max() - cdf.min())
    equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized)
    equalized_image = equalized_image.reshape(image.shape)
    equalized_image = equalized_image.astype(np.uint8)
    return equalized_image

image_path = 'C:/Users/Aliyan Sajid/Desktop/soldier.jpg'

image = cv2.imread(image_path)
equalized_image = histogram_sliding(image)

hist_original, bins_original = np.histogram(image.flatten(), 256, [0, 256])
hist_equalized, bins_equalized = np.histogram(equalized_image.flatten(), 256, [0, 256])

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
axs[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')
axs[0, 1].imshow(equalized_image, cmap='gray')
axs[0, 1].set_title('Equalized Image')
axs[0, 1].axis('off')
axs[1, 0].plot(hist_original, color='r')
axs[1, 0].set_title('Original Histogram')
axs[1, 0].set_xlabel('Pixel Intensity')
axs[1, 0].set_ylabel('Frequency')
axs[1, 1].plot(hist_equalized, color='b')
axs[1, 1].set_title('Equalized Histogram')
axs[1, 1].set_xlabel('Pixel Intensity')
axs[1, 1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()