import cv2 as cv
import numpy as np

img = cv.imread('girl.jpg', 0)
res = cv.bilateralFilter(img, 35, 25, 45)
res2 = cv.bilateralFilter(img, 35, 25, 15)
#bilateraFilter() 35,25,45 is:
#35 : size of matrix
#25 : distance sigme, to smooth items 
#15 : gray sigma, bigger and edge can't see
cv.imshow('origin', img)
cv.imshow('res', res)
cv.imshow('res2', res2)
cv.waitKey(0)
cv.destroyAllWindows()