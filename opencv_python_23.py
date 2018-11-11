import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#fft in numpy

img = cv.imread('dog.jpg', 0)
f = np.fft.fft2(img)
#trans img into frequence, fft
fshift = np.fft.fftshift(f)
fshift = np.fft.ifftshift(f)
#do fft shift to the fft image
#Shift zero-frequency component to center
#exchange 1 ang 3, 2 and 4
magnitude_spectrum = 20*np.log(np.abs(fshift))
#fu zhi
#if center is lighter big, it means image has many low frequcecy

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
