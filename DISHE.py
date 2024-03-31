import cv2
import numpy as np
import matplotlib.pyplot as plt

def dsihe(image, num_tiles=8):
    height, width = image.shape[:2]
    tile_height = height // num_tiles
    tile_width = width // num_tiles
    equalized_image = np.zeros_like(image)
    for i in range(num_tiles):
        for j in range(num_tiles):
            roi = image[i*tile_height:(i+1)*tile_height, j*tile_width:(j+1)*tile_width]
            equalized_roi = cv2.equalizeHist(roi)
            equalized_image[i*tile_height:(i+1)*tile_height, j*tile_width:(j+1)*tile_width] = equalized_roi
    return equalized_image

image_path = 'C:/Users/Aliyan Sajid/Desktop/soldier.jpg'

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is not None:
    dsihe_image = dsihe(image)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Input Image')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(dsihe_image, cmap='gray')
    plt.title('DSIHE Output')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.hist(image.flatten(), bins=256, range=[0, 256], color='r', alpha=0.7)
    plt.title('Input Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.subplot(1, 2, 2)
    plt.hist(dsihe_image.flatten(), bins=256, range=[0, 256], color='b', alpha=0.7)
    plt.title('DSIHE Output Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()