import cv2 as cv
import numpy as np

img = cv.imread('txbb.jpg')
b, g, r = cv.split(img)
#split the three channels of img
g = r
#exchange the red channel and green channe
imgnew = cv.merge([b, g, r])
#make a new merge img of b,g,r for rgb
cv.imshow('img', imgnew)
cv.waitKey(0)
cv.destroyAllWindows()