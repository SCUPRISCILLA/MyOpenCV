#opencv using matplotlib to show an image
#yang hai xin 2018 10/20

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

im1 = cv.imread('/home/priscilla/opencv_python/dog.jpg', 0)
#using imread() function to show a image
plt.imshow(im1, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])X
plt.show()