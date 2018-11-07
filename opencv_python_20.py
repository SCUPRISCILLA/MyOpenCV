import cv2 as cv
import numpy as np

img = cv.imread('ContactLens.tif')
img = cv.resize(img, (512, 512))
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

thresh = cv.adaptiveThreshold(imggray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 35, 15)
#matrix 35*35, and parameter is 15 to do a adaptive threshold to get a BW pic
image, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#findContours is to find the contours, return three : image is the image of contours
#contours is the position of contours
#hierarchy I don't know what used for...
print(len(contours))
for i in range(len(contours)):
	ground = np.zeros((512, 512), np.uint8)
	cv.drawContours(ground, contours, i, 255, 3)
	cv.imshow('contour'+str(i), ground)
	#cv.drawContours(ground, contours, -1, 255, 3)
	#to draw contours on the picture 'img'
	#-1 is to draw all contours, i is to show contours one by one
	#(0, 0, 255) is red
	#3 is the thin of line


cv.waitKey(0)
cv.destroyAllWindows()