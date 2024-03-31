import cv2
import numpy as np
import matplotlib.pyplot as plt

def shrink_histogram(image, target_min, target_max):
    hist, _ = np.histogram(image.flatten(), bins=256, range=[0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf / float(cdf.max())
    transfer_function = (cdf - cdf.min()) * (target_max - target_min) / (cdf.max() - cdf.min()) + target_min
    transfer_function = transfer_function.astype(np.uint8)
    equalized_image = transfer_function[image]
    return equalized_image

image_path = 'C:/Users/Aliyan Sajid/Desktop/soldier.jpg'

try:
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
except Exception as e:
    print("Error: Unable to load image.", e)
    image = None

if image is not None:
    shrunken_image = shrink_histogram(image, 50, 200)
    plt.figure(figsize=(10, 5))
    
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    
    plt.subplot(2, 2, 2)
    plt.hist(image.flatten(), bins=256, range=[0, 256], color='r')
    plt.title('Original Histogram')
    plt.xlim([0, 256])
    
    plt.subplot(2, 2, 3)
    plt.imshow(shrunken_image, cmap='gray')
    plt.title('Shrunken Image')
    
    plt.subplot(2, 2, 4)
    plt.hist(shrunken_image.flatten(), bins=256, range=[0, 256], color='b')
    plt.title('Shrunken Histogram')
    plt.xlim([0, 256])
    
    plt.tight_layout()
    plt.show()