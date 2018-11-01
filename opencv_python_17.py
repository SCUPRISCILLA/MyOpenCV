import cv2 as cv
import numpy as np

img = cv.imread('txbb.jpg', 0)

lap = cv.Laplacian(img, cv.CV_16S, ksize = 3)
#laplacian is er jie dao shu of image x and y then sum them
#also needs to convert uint8 into uint16
#ksize is the matrix size, 1 3 5 7
res = cv.convertScaleAbs(lap)

cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()