import cv2

def load_image_from_file(file_path):
    return cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

image_path = r"C:\Users\Aliyan Sajid\Desktop\Codes\insect.jpg"
image = load_image_from_file(image_path)

if image is None:
    print("Error: Image not found or unable to read the image.")
    exit()

_, global_thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)


cv2.imshow("Original Image", image)
cv2.imshow("Global Thresholded Image", global_thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()