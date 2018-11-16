import cv2 as cv
import numpy as np

imgorigin = cv.imread('pen.jpg')
imggray = cv.cvtColor(imgorigin, cv.COLOR_RGB2GRAY)
cv.imshow('gray', imggray)

canny = cv.Canny(imggray, 150, 200, apertureSize = 3) #do the canny to get a better edge
cv.imshow('canny', canny)

minLineLength = 200  #<200 is not a line
maxLineGap = 30 #<30 will be a same line
lines = cv.HoughLinesP(canny,1,np.pi/180,100,minLineLength,maxLineGap) #return begin point and end point
for line in lines:
	x1,y1,x2,y2 = line[0]
	cv.line(imgorigin,(x1,y1),(x2,y2),(0,255,0),2)

cv.imshow('res', imgorigin)
cv.waitKey(0)
cv.destroyAllWindows()