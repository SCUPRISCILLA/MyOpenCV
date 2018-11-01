import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while 1:
	ret, frame = cap.read()
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	res = cv.bilateralFilter(gray, 35, 25, 45)
	cv.imshow('frame', res)
	if cv.waitKey(1) & 0xFF ==ord('q'):  #press q to exit
		break

cap.release()
cv.destroyAllWindows()