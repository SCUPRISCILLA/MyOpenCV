import cv2 as cv
import numpy as np

img = cv.imread('txbb.jpg', 0)

x = cv.Sobel(img, cv.CV_16S, 1, 0)
#make a x direction sobel
#cv.CV_16S is tran uint8 to uint16, in order to make a large rang of gray
#if not cv.CV_16S, some gray value will less than 0 and bigger than 255, will be all gray
#1, 0  means x direction
y = cv.Sobel(img, cv.CV_16S, 0, 1)
#cv.Sobel only make one direction

absX = cv.convertScaleAbs(x)
#using x's absolute which is uint8
absY = cv.convertScaleAbs(y)

res = cv.addWeighted(absX, 0.5, absY, 0.5, 0)
#combine x and y by addweighted
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()