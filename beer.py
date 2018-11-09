import cv2 as cv
import numpy as np

img = cv.imread('./BEER/Good/1.tif')
H, W = img.shape[0:2]
#get size of img
X = int(H/10)
Y = int(W/10)
#resize factor
kernel = cv.getStructuringElement(cv.MORPH_RECT,(9, 9))
#make a kernel to do dilate

imgrgb = cv.resize(img, (X, Y))
#resize image which is too big
imggray = cv.cvtColor(imgrgb, cv.COLOR_BGR2GRAY)
imgbio = cv.bilateralFilter(imggray, 35, 40, 35)
#using bilaterafilter to reduce noise and background
thresh = cv.adaptiveThreshold(imggray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 17)
#using adaptive threshold to only have the beers
dilate = cv.dilate(thresh, kernel)
#matrix 35*35, and parameter is 15 to do a adaptive threshold to get a BW pic
#this will make beers logo to be 255
image, contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#get beers contours

print("the num of beers is " + str(len(contours)))
cv.imshow('oringin', imgrgb)
cv.imshow('dilate', dilate)
cv.waitKey(0)
cv.destroyAllWindows()
