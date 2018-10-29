import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
#open camera
while 1:   #make a video
	ret, frame = cap.read()
	#get frame from camera
	frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	frame = cv.medianBlur(frame, 5)
	#convert frame into gray and median filter
	th1 = cv.adaptiveThreshold(frame, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
	#using adaptive threshold to BW frame
	cv.imshow('camera2', th1)
	k = cv.waitKey(5)&0xff  #delay 5ms
	if k == 27:    #esc
		break
cv.destroyAllWindows()