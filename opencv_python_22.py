import cv2 as cv
import numpy as np

img = cv.imread('EX2.tif')
imgrgb = cv.resize(img, (512, 512))
imggray = cv.cvtColor(imgrgb, cv.COLOR_BGR2GRAY)
thresh = cv.adaptiveThreshold(imggray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 35, 15)
#matrix 35*35, and parameter is 15 to do a adaptive threshold to get a BW pic
image, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#find the contours of a BW pic
cnt = contours[3]
#using contour 4
ground = np.zeros((512, 512), np.uint8)
#make a black ground
cv.drawContours(ground, contours, 3, 255, 3)

hull = cv.convexHull(cnt)
#make a convex hull tubao
cv.polylines(imgrgb, [hull], True, (0, 255, 0), 2)
#draw convex hull
k = cv.isContourConvex(cnt)
#if is a convex, return True
print(k)

cv.imshow('rgb', imgrgb)
cv.imshow('contour', ground)
cv.imshow('origin', imggray)
cv.imshow('thr', thresh)
cv.waitKey(0)
cv.destroyAllWindows()