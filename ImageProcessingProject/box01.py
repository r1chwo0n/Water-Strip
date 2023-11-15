import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('photo/box1.png',cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# cv.imshow('Strip1',img)

laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(1,2,2),plt.imshow(laplacian,cmap='gray')
plt.title('Laplacian'),plt.xticks([]),plt.yticks([])

# plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray')
# plt.title('Sobel X'),plt.xticks([]), plt.yticks([])

# plt.subplot(2,2,4),plt.imshow(sobely,cmap='gray')
# plt.title('Sobel Y'),plt.xticks([]), plt.yticks([])



plt.show()