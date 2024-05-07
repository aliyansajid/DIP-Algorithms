import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import cv2

image_path = r'C:\Users\Aliyan Sajid\Desktop\Codes\insect.jpg'
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_array = np.array(image_rgb)
pixels = image_array.reshape((-1, 3))

kmeans_cluster = KMeans(n_clusters=5)
kmeans_labels = kmeans_cluster.fit_predict(pixels)
kmeans_clustered_image = kmeans_labels.reshape(image_array.shape[:2])

plt.figure(figsize=(6, 6))
plt.subplot(1, 2, 1)
plt.imshow(image_array)
plt.title('Original Image')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(kmeans_clustered_image, cmap='viridis')
plt.title('K-means Clustering')
plt.axis('off')
plt.show()