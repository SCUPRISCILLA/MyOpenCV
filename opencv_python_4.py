import cv2 as cv
import numpy as np

img = cv.imread('dog.jpg')
print(img.shape)
nose = img[40:80, 40:80]   
#take a picese of image
cv.imshow('nose', nose)

img[:, :, 1] = 0
img[:, :, 2] = 0
cv.imshow('blue', img)
#make the BGR channel's Green ang Red into 0
#it will make the image be Blue

constant = cv.copyMakeBorder(img, 100, 100, 100, 100, cv.BORDER_CONSTANT, value=[0, 255, 0])
#add a border to image
#the border is added 100 to up, 100 to buttom, 100 to right...
#cv.BORDER_CONSTANT is one of the border interpolation(cha zhi) algorithm, value is green
#there are so many border algorithm
cv.imshow('border', constant)  

cv.waitKey(0)
cv.destroyAllWindows()