import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

im1 = cv.imread('dog.jpg')
H = np.float32([[1, 0, 10], [0, 1, 10]])
#make a matrix, which will makes the image move x+10, y+10
# 1 0 10    x   x+10
# 0 1 10  * y = y+10
#           1   
row, col = im1.shape[0:2]
#shape ruturns a tuple, [x y channel]
#using shape[:2] can get the 0 1 element,[:2]is 0 1
print(row, col)
im1move = cv.warpAffine(im1, H, (row, col))
#do a affine by H matrix, it will make a translation(ping yi)
#im1move = H*im1
res = cv.resize(im1move, (2*col, 2*row), interpolation = cv.INTER_LINEAR)
#resize the image, it will become twice bigger than origin
#and the interpolation algorithm is inter_linear which is fast of bigger
cv.imshow('res1', res)
cv.waitKey(0)
cv.destroyAllWindows()
# res = cv.warpAffine(im1, H, (row, col))
# cv.imshow('im1', im1)
# cv.imshow('im2', res)
# cv.waitKey(0)
# cv.destroyAllWindows()