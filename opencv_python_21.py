import cv2 as cv
import numpy as np

img = cv.imread('ContactLens.tif')
img = cv.resize(img, (512, 512))
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
thresh = cv.adaptiveThreshold(imggray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 35, 15)
#matrix 35*35, and parameter is 15 to do a adaptive threshold to get a BW pic
image, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[3]
m = cv.moments(cnt)
#cv.moments() is to caculate ju of a contour
print(m)
cx = int(m['m10']/m['m00'])
cy = int(m['m01']/m['m00'])
#using ju to caculate gravity point
print(cx, cy)
area = cv.contourArea(cnt)
#caculate area of contour which is equal to m['m00']
print(area)
print(m['m00'])
#they are same
perimeter = cv.arcLength(cnt, True)
print(perimeter)