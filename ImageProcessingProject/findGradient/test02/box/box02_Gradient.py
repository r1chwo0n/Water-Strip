import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = cv.imread('findGradient/test02/box/box2.png', cv.COLOR_BGR2RGB)
image2 = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

# sobel_x = cv.Sobel(image2, cv.CV_64F, 1, 0, ksize=3)
# sobel_y = cv.Sobel(image2, cv.CV_64F, 0, 1, ksize=3)
# gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# threshold_value = 100
# white_gradient_mask = gradient_magnitude > threshold_value

# white_mask = np.zeros_like(image2)
# white_mask [white_gradient_mask] = 255

# plt.subplot(1,2,1),plt.imshow(image2,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])

# plt.subplot(1,2,2),plt.imshow(white_mask,cmap='gray')
# plt.title('White gradient mask'),plt.xticks([]),plt.yticks([])

cv.imshow('image',image2)
cv.waitKey(0)