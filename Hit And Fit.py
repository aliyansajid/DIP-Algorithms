import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'C:/Users/Aliyan Sajid/Desktop/Codes/house.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)

struct_elem = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

def hit_and_fit(image, struct_elem):
    hit = cv2.erode(image, struct_elem)
    fit = cv2.dilate(image, struct_elem)
    return hit, fit

hit_image, fit_image = hit_and_fit(binary_image, struct_elem)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(binary_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Hit Algorithm Applied')
plt.imshow(hit_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Fit Algorithm Applied')
plt.imshow(fit_image, cmap='gray')
plt.axis('off')
plt.show()