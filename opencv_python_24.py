import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#fft in opencv and fftshift in numpy

img = cv.imread('dog.jpg', 0)
dft = cv.dft(np.float32(img), flags = cv.DFT_COMPLEX_OUTPUT)
#*******cv2.dft needs input image is a float 32 matrix***********
dftshift = np.fft.fftshift(dft)

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()