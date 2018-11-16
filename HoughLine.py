import cv2 as cv
import numpy as np

imgorigin = cv.imread('pen.jpg')
imggray = cv.cvtColor(imgorigin, cv.COLOR_RGB2GRAY)
cv.imshow('gray', imggray)

canny = cv.Canny(imggray, 150, 200, apertureSize = 3) #do the canny to get a better edge
cv.imshow('canny', canny)

lines = cv.HoughLines(canny, 1, np.pi/180, 200) #Standard Hough lines, which is slow, return rho and theta

for line in lines:
	rho, theta = line[0]
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a))
	cv.line(imgorigin,(x1,y1),(x2,y2),(0,0,255),2) #draw the lines

cv.imshow('res', imgorigin)

cv.waitKey(0)
cv.destroyAllWindows()