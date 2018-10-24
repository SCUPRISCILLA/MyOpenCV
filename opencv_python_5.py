#opencv using cv.addWeighted() to make a ppt pic changing

import cv2 as cv
import numpy as np

e1 = cv.getTickCount()

im1 = cv.imread('dog.jpg', 0)
im2 = cv.imread('txbb.jpg', 0)
im2small = im2[200:322, 300:414]
k = 1
for i in range(1, 51):  #range(1, 11) means: i = 1/2/3..../10
	k = k-0.02
	im3 = cv.addWeighted(im1, k, im2small, 1-k, 0)
	cv.imshow('winname', im3)
	cv.waitKey(100)

e2 = cv.getTickCount()
time = (e2 - e1)/cv.getTickFrequency()
print(time)

cv.waitKey(0)
cv.destroyAllWindows()