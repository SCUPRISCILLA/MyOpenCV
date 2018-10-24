#opencv using computer camera
#yang hai xin 2018 10/20

import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
font = cv.FONT_HERSHEY_SIMPLEX


while True:
	ret, frame = cap.read()
	#print(ret)  #cap.read() first return is a boolean True/False
	#print(frame)  #cap.read() second return is a matrix of image
	cv.putText(frame, 'Brilliant in every way.', (50,250), font, 2, (0, 0, 0), 2, cv.LINE_AA)
	cv.putText(frame, 'iPhone XR', (50,100), font, 2, (255, 255, 255), 2, cv.LINE_AA)
	#put a text 'YHX' on the image /frame
	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	cv.imshow('frame', gray)
	if cv.waitKey(1) & 0xFF ==ord('q'):
		break

cap.release()
cv.destroyAllWindows()