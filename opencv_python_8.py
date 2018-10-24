import cv2 as cv
import numpy as np

img = cv.imread('dog.jpg')
row, col = img.shape[:2]

M = cv.getRotationMatrix2D((col/2, row/2), 45, 1)
#make a rotation matrix
#(col/3,row/2) is the rotation center, 45 is rotation angle
#ang 1 is the scaling ratio
dst = cv.warpAffine(img, M, (2*col, 2*row))
#this function is to do warpaffine
#using the affine matrix M 
#and final image is 2col, 2row size
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()