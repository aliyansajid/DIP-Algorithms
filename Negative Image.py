from PIL import Image
import matplotlib.pyplot as plt

def negative_image(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to grayscale if it's in color
    if image.mode != 'L':
        image = image.convert('L')
    
    # Get image data
    image_data = list(image.getdata())
    
    # Create negative image data
    negative_data = [(255 - pixel) for pixel in image_data]
    
    # Create negative image
    negative_image = Image.new('L', image.size)
    negative_image.putdata(negative_data)
    
    # Display images side by side
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    
    # Show the original image
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')
    
    # Show the negative image
    axes[1].imshow(negative_image, cmap='gray')
    axes[1].set_title('Negative Image')
    axes[1].axis('off')

    plt.show()

# Example usage
image_path = r'C:\Users\Aliyan Sajid\Downloads\pexels-mike-bird-170811.jpg'
negative_image(image_path)