import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('dog.jpg')
kernel = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)
#-1 is to make sure dst has the same deep with img
#-1 is means dst and img are same bit of pixel

# plt.subplot(121),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
# plt.xticks([]), plt.yticks([])
# plt.show()
cv.imshow('res', dst)
cv.waitKey(0)
cv.destroyAllWindows()