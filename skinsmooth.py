import cv2 as cv
import numpy as np

img = cv.imread('girl.jpg', 0)
res = cv.bilateralFilter(img, 35, 25, 45)
cv.imshow('origin', img)
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()