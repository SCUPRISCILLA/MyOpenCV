import cv2 as cv
import numpy as np

img = cv.imread('dog.jpg')
print(img.shape)
nose = img[40:80, 40:80]   #take a picese of image
cv.imshow('nose', nose)

img[:, :, 1] = 0
img[:, :, 2] = 0
cv.imshow('blue', img)

constant = cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_CONSTANT, value=[255, 0, 0])
cv.imshow('border', constant)  #add a border to image

cv.waitKey(0)
cv.destroyAllWindows()