# import cv2 module
import cv2
while(1):
# resd the image
    img = cv2.imread('image/32,141,50.png')
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# shape prints the tuple (height,weight,channels)
# print(img.shape)
  
# img will be a numpy array of the above shape
# print(img)
    cv2.imshow('RGB Image',img)
    cv2.imshow('HSV image',hsv_img)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break
print(img[0][0])
print(hsv_img[0][0])

cv2.destroyAllWindows()
