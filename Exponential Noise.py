import cv2
import numpy as np
import matplotlib.pyplot as plt

def exponential_noise(image, scale=25):
    noise = np.random.exponential(scale, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

image_path = r'C:\Users\Aliyan Sajid\Desktop\soldier.jpg'
image = cv2.imread(image_path)
noisy_image = exponential_noise(image)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
plt.title('Exponential Noise')
plt.axis('off')
plt.show()