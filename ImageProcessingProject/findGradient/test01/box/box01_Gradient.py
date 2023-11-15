import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Load the image (replace 'your_image.jpg' with the path to your image)
image = cv.imread('findGradient/test01/box/box1.png')

# Compute the gradient magnitude using cv.Sobel
sobel_x = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=3)
sobel_y = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# Threshold the gradient magnitude to identify white gradients
threshold_value = 100  # Adjust this threshold value as needed
white_gradient_mask = gradient_magnitude > threshold_value

# Create an output image showing the identified white gradients
white_mask = np.zeros_like(image)
white_mask [white_gradient_mask] = 255  # Set the white gradient regions to white

# Plotting images to show
plt.subplot(1,2,1),plt.imshow(image,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(1,2,2),plt.imshow(white_mask,cmap='gray')
plt.title('White gradient mask'),plt.xticks([]),plt.yticks([])

plt.show()