import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('dog.jpg')
kernel = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)
#filter2D is to use kernel to do image filter
#kernel could be guassian, average, or median
#-1 is to make sure dst has the same deep with img
#-1 is means dst and img are same bit of pixel
cv.imshow('res', dst)
cv.waitKey(0)
cv.destroyAllWindows()