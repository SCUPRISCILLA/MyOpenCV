import cv2 as cv
import numpy as np

img = cv.imread('dog.jpg')
row, col = img.shape[:2]

pts1 = np.float32([[56, 65], [40, 40], [28, 100], [66, 99]])
pts2 = np.float32([[0, 0], [0, 100], [100, 0], [100, 100]])
#to select four points to make a transform mask
#pts1 is the source, and pts2 is the detination

M = cv.getPerspectiveTransform(pts1, pts2)
#make a perspective transform mask by four points

res = cv.warpPerspective(img, M, (100, 100))
#using mask M to do a perspective transform

cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()