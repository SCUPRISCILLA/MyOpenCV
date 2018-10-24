import cv2 as cv
import numpy as np

img = cv.imread('dog.jpg')
row, col = img.shape[:2]
print(row, col)

pts1 = np.float32([[50, 50], [100, 50], [50, 100]])
pts2 = np.float32([[60, 50], [120, 50], [100, 100]])
#pts1: select three points from the origin pic
#pts2: pts1's points' new position in result pic
#in this way, we can do affine by changing the pts2's position

M = cv.getAffineTransform(pts1, pts2)
#caculate the matrix which makes pts1 to pts2
#pts2 = M * pts1
res = cv.warpAffine(img, M, (3*row, 3*col))
#do affine by matrix M, which make pts1 to pts2
#res = M * img

cv.imshow('img', img)
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()
