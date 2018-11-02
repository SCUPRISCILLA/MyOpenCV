import cv2 as cv
import numpy as np

img = cv.imread('txbb.jpg', 0)
res = cv.Canny(img, 50, 150, L2gradient = True)
#cv.Canny 50 is the low threshold, <50 will become 0
#150 is the up threshold, >150 will become 255
#between 50 and 150 and is connected to edge will become 255
#L2gradient : True is sqrt(x^2+y^2), False is x^2+y^2
cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()