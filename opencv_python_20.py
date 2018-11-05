import cv2 as cv
import numpy as np

img = cv.imread('txbb.jpg', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)
image, contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
img1 = cv.drawContours(img, contours, 3, (0, 255, 0), 3)
cv.imshow('res', img1)
cv.waitKey(0)
cv.destroyAllWindows()