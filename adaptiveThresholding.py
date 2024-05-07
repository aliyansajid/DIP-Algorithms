import cv2

def load_image_from_file(file_path):
    return cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

image_path = r"C:\Users\Aliyan Sajid\Desktop\Codes\insect.jpg"
image = load_image_from_file(image_path)

if image is None:
    print("Error: Image not found or unable to read the image.")
    exit()


try:
    adaptive_thresholded = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
except cv2.error as e:
    print("Error occurred during adaptive thresholding:", e)
    adaptive_thresholded = np.zeros_like(image)


cv2.imshow("Original Image", image)
cv2.imshow("Adaptive Thresholded Image", adaptive_thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()