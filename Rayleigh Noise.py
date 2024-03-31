import cv2
import numpy as np
import matplotlib.pyplot as plt

def rayleigh_noise(image, scale=25):
    noise = np.random.rayleigh(scale, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image

image_path = r'C:\Users\Aliyan Sajid\Desktop\soldier.jpg'
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
noisy_image = rayleigh_noise(image)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(noisy_image)
plt.title('Image with Rayleigh Noise')
plt.axis('off')
plt.show()