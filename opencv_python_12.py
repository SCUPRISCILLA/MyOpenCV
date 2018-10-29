import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('txbb.jpg', 0)
#0 is to load as gray, if >0, load as a color three channels
ret, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
#127 is the threshold, when > 127, then become 255, binary is BW
ret, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
#BINARY_INV is BW inverse, <127 become 255
ret, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
#>127 become 255, and <127 is not change
ret, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
#<127 become 0, and >127 is not change
ret, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
#>127 become 0, and <127 is not change
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(0, 6):   #i = 0 1 2 3 4 5
	plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
	plt.title(titles[i])
	plt.xticks([]),plt.yticks([])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()