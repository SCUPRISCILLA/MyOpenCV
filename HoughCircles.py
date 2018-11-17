import cv2 as cv
import numpy as np

imgorigin = cv.imread('ContactLens.tif', 0)
H, W = imgorigin.shape[0:2]
imgsmall = cv.resize(imgorigin, (int(H/3), int(W/3)), cv.INTER_LINEAR)
circles = cv.HoughCircles(imgsmall, cv.HOUGH_GRADIENT, 1, 45, param1 = 50, param2 = 30, minRadius = 150)
#cv.HoughCircles(image, method, dp, minDist, circles, param1, param2, minRadius, maxRadius)
#method: Hough Gradient is tidu
#dp = 1 means the accumulator has the same resolution(fen bian lu) as the input image.
#minDist: Minimum distance between the centers of the detected circles.
#param1: it is the higher threshold of the two passed to the Canny() edge detector
#used to do edge detect
#param2: it is the accumulator threshold for the circle centers
#The smaller it is, the more false circles may be detected
#minRadius – Minimum circle radius.
#maxRadius – Maximum circle radius.
circles = np.uint16(np.around(circles))
#cv.HoughCircles() will return a vector
#(x, y, radius)

for i in circles[0, : ]:
	# draw the outer circle i[0] is x, i[1] is y, i[2] is radius
	cv.circle(imgsmall, (i[0], i[1]), i[2], (0, 255, 0), 2)
	# draw the center of the circle
	cv.circle(imgsmall, (i[0], i[1]), 2, (0, 0, 255), 3)
cv.imshow('detected circles', imgsmall)

cv.waitKey(0)
cv.destroyAllWindows()