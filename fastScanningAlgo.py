import numpy as np
import matplotlib.pyplot as plt
import cv2

image_path = 'C:/Users/Aliyan Sajid/Desktop/Codes/insect.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = 50

def fast_scan(image, threshold):
    regions = []
    height, width = image.shape[:2]
    labels = np.zeros((height, width), dtype=int)
    current_label = 1
    
    def get_label(x, y):
        if x < 0 or y < 0 or x >= width or y >= height:
            return 0
        return labels[y, x]
    
    for y in range(height):
        for x in range(width):
            if labels[y, x] != 0:
                continue
            intensity = image[y, x]
            left_label = get_label(x - 1, y)
            above_label = get_label(x, y - 1)
            if abs(intensity - image[y, x - 1]) < threshold and left_label != 0:
                labels[y, x] = left_label
            elif abs(intensity - image[y - 1, x]) < threshold and above_label != 0:
                labels[y, x] = above_label
            else:
                labels[y, x] = current_label
                current_label += 1
                
    for y in range(height):
        for x in range(width):
            current_label = labels[y, x]
            if current_label != 0:
                neighbors = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
                for nx, ny in neighbors:
                    if 0 <= nx < width and 0 <= ny < height and labels[ny, nx] != 0:
                        neighbor_label = labels[ny, nx]
                        if neighbor_label != current_label:
                            min_label = min(current_label, neighbor_label)
                            max_label = max(current_label, neighbor_label)
                            labels[labels == max_label] = min_label
    
    unique_labels = np.unique(labels)
    unique_labels = unique_labels[unique_labels != 0]
    
    for label in unique_labels:
        region = np.zeros_like(gray_image, dtype=np.uint8)
        region[labels == label] = 255
        regions.append(region)
    
    return regions

merged_regions = fast_scan(gray_image, threshold)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')
for region in merged_regions:
    plt.contour(region, colors='r')
plt.title('Merged Regions')
plt.axis('off')

plt.tight_layout()
plt.show()