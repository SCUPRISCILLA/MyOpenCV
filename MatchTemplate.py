import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

imgrgb = cv.imread('txbb.jpg')
img = cv.cvtColor(imgrgb, cv.COLOR_RGB2GRAY)
template = cv.imread('face.jpg', 0)
h, w = template.shape[0:2]

res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
cv.imshow('winname', res)
thre = 0.8
loc = np.where(res >= thre)
for pt in zip(*loc[::-1]): 
	right_bottom = (pt[0] + w, pt[1] + h) 
	cv.rectangle(imgrgb, pt, right_bottom, (0, 0, 255), 2)
cv.imshow('res', imgrgb)
cv.waitKey(0)
cv.destroyAllWindows()