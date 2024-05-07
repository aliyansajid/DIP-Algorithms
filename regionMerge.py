import numpy as np
import matplotlib.pyplot as plt
import cv2

image_path = 'C:/Users/Aliyan Sajid/Desktop/Codes/insect.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def split_regions(image, threshold):
    regions = []
    height, width = image.shape[:2]
    
    def should_split(region):
        return region.std() > threshold
    
    def split_region(region, x, y, w, h):
        if should_split(region):
            split_width = w // 2
            split_height = h // 2
            
            sub_regions = [
                (x, y, split_width, split_height),
                (x + split_width, y, split_width, split_height),
                (x, y + split_height, split_width, split_height),
                (x + split_width, y + split_height, split_width, split_height)
            ]
            
            for sub_x, sub_y, sub_w, sub_h in sub_regions:
                sub_region = image[sub_y:sub_y+sub_h, sub_x:sub_x+sub_w]
                if sub_region.size > 0:
                    split_region(sub_region, sub_x, sub_y, sub_w, sub_h)
        else:
            regions.append((x, y, w, h))
    
    split_region(gray_image, 0, 0, width, height)
    
    return regions

def merge_regions(image, regions, threshold):
    merged_regions = []
    
    for x, y, w, h in regions:
        region_mean = np.mean(image[y:y+h, x:x+w])
        
        if not np.isnan(region_mean):
            for idx, (nx, ny, nw, nh) in enumerate(merged_regions):
                neighbor_mean = np.mean(image[ny:ny+nh, nx:nx+nw])
                diff = abs(region_mean - neighbor_mean)
                
                if not np.isnan(neighbor_mean) and diff < threshold:
                    merged_regions[idx] = (min(x, nx), min(y, ny), max(w, nw), max(h, nh))
                    break
            else:
                merged_regions.append((x, y, w, h))
    
    return merged_regions

regions = split_regions(gray_image, threshold=20)

merged_regions = merge_regions(gray_image, regions, threshold=50)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap='gray')
for x, y, w, h in merged_regions:
    plt.plot([x, x+w, x+w, x, x], [y, y, y+h, y+h, y], 'r')
plt.title('Merged Regions')
plt.axis('off')
plt.tight_layout()
plt.show()