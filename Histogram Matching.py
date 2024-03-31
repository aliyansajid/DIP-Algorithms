import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_matching(input_image, target_histogram):
    input_hist = cv2.calcHist([input_image], [0], None, [256], [0, 256])
    target_hist = target_histogram
    input_hist /= input_hist.sum()
    target_hist /= target_hist.sum()
    input_cdf = input_hist.cumsum()
    target_cdf = target_hist.cumsum()
    mapping = np.interp(input_cdf, target_cdf, np.arange(256))
    matched_image = mapping[input_image]
    return matched_image.astype(np.uint8)

input_image_path = r"C:\Users\Aliyan Sajid\Desktop\soldier.jpg"
target_image_path = r"C:\Users\Aliyan Sajid\Desktop\car.jpg"

try:
    input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    target_image = cv2.imread(target_image_path, cv2.IMREAD_GRAYSCALE)
    target_histogram = cv2.calcHist([target_image], [0], None, [256], [0, 256])
    matched_image = histogram_matching(input_image, target_histogram)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(input_image, cmap='gray')
    plt.title('Input Image')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(matched_image, cmap='gray')
    plt.title('Histogram Matched Image')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(input_image.flatten(), bins=256, range=[0, 256], color='r', alpha=0.7)
    plt.title('Input Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.subplot(1, 2, 2)
    plt.hist(matched_image.flatten(), bins=256, range=[0, 256], color='b', alpha=0.7)
    plt.title('Matched Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

except Exception as ex:
    print("An error occurred:", ex)