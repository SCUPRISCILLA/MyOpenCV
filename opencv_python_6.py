#opencv track red green bule thing

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while(1):
	ret, frame = cap.read()
	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	#convert RGB to HSV

	lower_red = np.array([0, 50, 50])
	upper_red = np.array([10, 255, 255])
	mask_red = cv.inRange(hsv, lower_red, upper_red)
	#make a mask by hsv lower to upper
	#inrang function is to make a mask which is 1 of in, 0 of out
	#so items in mask will be keep origin, out mask will be 0 black
	#choose the HSV: H from 0 to 10 degree(du), which is red
	#and the S ang V is from 50 to 255, it is a standard

	lower_green = np.array([35, 50, 50])
	upper_green = np.array([77, 255, 255])
	mask_green = cv.inRange(hsv, lower_green, upper_green)

	lower_blue = np.array([110, 50, 50])
	upper_blue = np.array([130, 255, 255])
	mask_blue = cv.inRange(hsv, lower_blue, upper_blue)

	res1 = cv.bitwise_and(frame, frame, mask = mask_red)
	#to do a bit and, using mask to and frame to get res1
	#it will make the res1 only show the items in mask
	#out of the make will be 0, which is black
	res2 = cv.bitwise_and(frame, frame, mask = mask_green)

	res3 = cv.bitwise_and(frame, frame, mask = mask_blue)

	res4 = cv.add(res1, res2)
	res5 = cv.add(res4, res3)

	cv.imshow('res', res5)
	k = cv.waitKey(5)&0xFF
	if k == 27:    #esc
		break
cv.destroyAllWindows()