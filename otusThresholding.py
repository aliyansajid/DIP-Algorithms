import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = r'C:\Users\Aliyan Sajid\Desktop\Codes\insect.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found or unable to read the image.")
    exit()

if len(image.shape) > 2:
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    image_gray = image

_, otsu_thresholded = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

if len(otsu_thresholded.shape) < 3:
    otsu_thresholded = cv2.cvtColor(otsu_thresholded, cv2.COLOR_GRAY2BGR)

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
ax1.set_title('Original Image')
ax1.axis('off')

ax3.imshow(cv2.cvtColor(otsu_thresholded, cv2.COLOR_BGR2RGB))
ax3.set_title("Otsu's Thresholded")
ax3.axis('off')

plt.show()