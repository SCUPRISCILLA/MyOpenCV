#opencv showing the image items and change pix

import cv2 as cv
import numpy as np
img = cv.imread('dog.jpg')
px = img[100, 100]
print(px)       
blue = img[100, 100, 0]
print(blue)
print(img.item(100, 100, 0))
img.itemset((100, 100, 0), 100)
print(img.item(100, 100, 0))
print(img.shape)
print(img.size)  #row * col = the number of pix
print(img.dtype) #date type uint8 etc