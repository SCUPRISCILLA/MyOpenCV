import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

sobel_x = np.array([[-1, 0, 1],
					[-2, 0, 2],
					[-1, 0, 1]])  # sobel in x direction

sobel_y = np.array([[-1,-2,-1],
					[0, 0, 0],
					[1, 2, 1]])  # sobel in y direction

fft_x = np.fft.fft2(sobel_x)  #y direction fft
fft_y = np.fft.fft2(sobel_y)  #x direction fft

fshift_x = np.fft.fftshift(fft_x)
fshift_y = np.fft.fftshift(fft_y)

magnitude_spectrum_x = np.log(np.abs(fshift_x)+1)
magnitude_spectrum_y = np.log(np.abs(fshift_y)+1)

plt.subplot(121),plt.imshow(magnitude_spectrum_x, cmap = 'gray')
plt.title('sobel x'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum_y, cmap = 'gray')
plt.title('sobel y'), plt.xticks([]), plt.yticks([])
plt.show()
