import cv2
import numpy as np
import matplotlib.pyplot as plt

def bbhe(image):
    h, w = image.shape
    hist, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf / float(cdf.max())
    midpoint = np.argmax(cdf_normalized > 0.5)
    lower_cdf = cdf_normalized[midpoint]
    lower_cdf_mapping = (midpoint / 2) * cdf_normalized[:midpoint] / lower_cdf
    upper_cdf = cdf_normalized[-1] - lower_cdf
    upper_cdf_mapping = (midpoint / 2) + (255 - midpoint) * (cdf_normalized[midpoint:] - lower_cdf) / upper_cdf
    mapping = np.concatenate((lower_cdf_mapping, upper_cdf_mapping))
    equalized_image = mapping[image]
    return equalized_image.astype(np.uint8)

image_path = 'C:/Users/Aliyan Sajid/Desktop/soldier.jpg'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
equalized_image = bbhe(image)

plt.figure(figsize=(12, 6))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('BBHE Equalized Image')
plt.axis('off')
plt.subplot(2, 2, 3)
plt.hist(image.flatten(), bins=256, range=[0, 256], color='r', alpha=0.7)
plt.title('Original Histogram')
plt.xlim([0, 256])
plt.subplot(2, 2, 4)
plt.hist(equalized_image.flatten(), bins=256, range=[0, 256], color='b', alpha=0.7)
plt.title('BBHE Equalized Histogram')
plt.xlim([0, 256])
plt.tight_layout()
plt.show()