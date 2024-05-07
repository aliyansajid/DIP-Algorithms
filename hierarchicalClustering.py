import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram
import cv2

image_path = 'C:/Users/Aliyan Sajid/Desktop/Codes/insect.jpg'
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

scale_percent = 10
width = int(gray_image.shape[1] * scale_percent / 100)
height = int(gray_image.shape[0] * scale_percent / 100)
dim = (width, height)
resized_image = cv2.resize(gray_image, dim, interpolation=cv2.INTER_AREA)

X = resized_image.reshape((-1, 1))
clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=0).fit(X)

def plot_dendrogram(model, **kwargs):
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count
    linkage_matrix = np.column_stack([model.children_, model.distances_, counts]).astype(float)
    dendrogram(linkage_matrix, **kwargs)

plt.figure(figsize=(10, 5))
plt.title('Hierarchical Clustering Dendrogram')
plot_dendrogram(clustering, truncate_mode='level', p=3)
plt.xlabel('Number of points in node (or index of point if no parenthesis).')
plt.savefig('dendrogram.png')
plt.show()