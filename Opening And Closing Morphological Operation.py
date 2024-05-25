import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/Aliyan Sajid/Desktop/Codes/house.jpg', 0)
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.figure(figsize=(15, 5))
plt.subplot(131), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(132), plt.imshow(opening, cmap='gray'), plt.title('Opening')
plt.subplot(133), plt.imshow(closing, cmap='gray'), plt.title('Closing')
plt.show()