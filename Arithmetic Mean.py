import cv2
import numpy as np
import matplotlib.pyplot as plt

def arithmetic_mean_filter(image, window_size):
    return cv2.blur(image, (window_size, window_size))

image_path = r'C:\Users\Aliyan Sajid\Desktop\soldier.jpg'

image = cv2.imread(image_path)
window_size = 5

filtered_image = arithmetic_mean_filter(image, window_size)
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original Image')
axs[0].axis('off')
axs[1].imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
axs[1].set_title('Filtered Image')
axs[1].axis('off')     
plt.show()