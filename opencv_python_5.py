#opencv using cv.addWeighted() to make a ppt pic changing

import cv2 as cv
import numpy as np

e1 = cv.getTickCount()
#set a tickcount to record the time

im1 = cv.imread('dog.jpg', 0)
im2 = cv.imread('txbb.jpg', 0)
im2small = im2[200:322, 300:414]
#cut the im2, only use 200 to 322 rows and 300 to 414 cols
k = 1
for i in range(1, 51):  #range(1, 51) means: i = 1/2/3..../50
	k = k-0.02
	#50 * 0.02 = 1
	im3 = cv.addWeighted(im1, k, im2small, 1-k, 0)
	#addweighted is to make a algorithm:
	#im3 = im1 * k + im2small * (1-k) + 0
	cv.imshow('winname', im3)
	cv.waitKey(100)
	#delay 100 ms, in order to see the image
	#if not delay, it will be very fast that we can't see the process

e2 = cv.getTickCount()
#set another tickcount
time = (e2 - e1)/cv.getTickFrequency()
#to caculate the time
print(time)

cv.waitKey(0)
cv.destroyAllWindows()