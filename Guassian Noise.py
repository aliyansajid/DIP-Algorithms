import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_noise(image, mean=0, std=25):
    noisy_image = np.zeros(image.shape, np.uint8)
    cv2.randn(noisy_image, mean, std)
    noisy_image = cv2.add(image, noisy_image)
    return noisy_image

image_path = r'C:\Users\Aliyan Sajid\Desktop\soldier.jpg'
image = cv2.imread(image_path)

if image is not None:
    noisy_image = gaussian_noise(image)
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
    plt.title('Gaussian Noise')
    plt.axis('off')
    plt.show()
else:
    print("Failed to load the image.")