import cv2 as cv
import numpy as np

img = cv.imread('dog.jpg', 0)

blur = cv.blur(img, (13, 13))
#do a average of 13x13 matrix
blur_g = cv.GaussianBlur(img, (13, 13), 0)
#do a guassian blur of 13x13 matrix
blur_m = cv.medianBlur(img, 13)
#do a median blur of 13x13
blur_b = cv.bilateralFilter(img, 9, 75, 75)
#do the bilateralFilter
cv.imshow('origin', img)
cv.imshow('blur', blur)
cv.imshow('guassian', blur_g)
cv.imshow('medianBlur', blur_m)
cv.imshow('bilateralFilter', blur_b)
cv.waitKey(0)
cv.destroyAllWindows()