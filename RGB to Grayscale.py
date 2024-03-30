import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_normalization(image):
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calculate the histogram of the image
    hist, bins = np.histogram(image.flatten(), 256, [0,256])
    
    # Calculate cumulative distribution function (CDF) of the histogram
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    
    # Perform histogram normalization
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    
    # Map the pixels to their new intensity values using the normalized CDF
    normalized_image = cdf[image]
    
    return normalized_image

# Load an image
image = cv2.imread(r'C:\Users\Aliyan Sajid\Downloads\pexels-mike-bird-170811.jpg')

# Perform histogram normalization
normalized_image = histogram_normalization(image)

# Display the original and normalized images side by side
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(normalized_image, cmap='gray')
plt.title('Normalized Image')
plt.axis('off')

plt.show()