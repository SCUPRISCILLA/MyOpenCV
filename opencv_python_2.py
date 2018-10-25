#opencv using computer camera
#yang hai xin 2018 10/20

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SIMPLEX

while True:
	ret, frame = cap.read()
	#cap.read() to capture a video frame
	cv.putText(frame, 'Brilliant in every way.', (50,250), font, 2, (0, 0, 0), 2, cv.LINE_AA)
	cv.putText(frame, 'iPhone XR', (50,100), font, 2, (255, 255, 255), 2, cv.LINE_AA)
	#put a text 'YHX' on the image /frame
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	cv.imshow('frame', gray)
	#show video frame by frame
	#cv.waitKey(n)
	#if n > 0, it will delay n ms, then the video will be low FPS

	if cv.waitKey(1) & 0xFF ==ord('q'):  #press q to exit
		break

cap.release()
cv.destroyAllWindows()