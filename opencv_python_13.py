import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('book.jpg', 0)
img = cv.medianBlur(img, 5)
#median filter
hist = cv.calcHist([img], [0], None, [256], [0, 256])
# plt.plot(hist)
# plt.show()
#show the hist to choose a better threshold, like 200
ret, th1 = cv.threshold(img, 200, 255, cv.THRESH_BINARY)
print(ret)
#ret is the threshold
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, 15)
#make a 31x31 matrix to caculte the average to be the threshold
#the bigger the matrix, the better the BW, and the param should be bigger to reduce noise
#if the matrix is too small, it will become a edge detection

cv.imshow('book1', th1)
cv.imshow('book2', th2)
cv.waitKey(0)
cv.destroyAllWindows()