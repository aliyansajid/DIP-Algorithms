import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = r"C:\Users\Aliyan Sajid\Desktop\Codes\insect.jpg"
img = cv2.imread(img_path)

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    threshold = 0.01 * dst.max()
    corner_img = np.zeros_like(img)
    corner_img[dst > threshold] = [255, 255, 255]

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(corner_img, cv2.COLOR_BGR2RGB))
    plt.title('Corners Detected (White on Black)')
    plt.axis('off')

    plt.show()
else:
    print("Failed to load the image from the provided path.")