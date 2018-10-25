#opencv showing the image items and change pix

import cv2 as cv
import numpy as np
img = cv.imread('dog.jpg')
px = img[100, 100]
#img[x, y] is to select the position x,y
#and return this position's RGB in tuple
print('px=', px)       
blue = img[100, 100, 0]
#return is reverse
#RGB but return BGR in 0 1 2
#so img[,,0] is Blue
print('blue=', blue)
print(img.item(100, 100, 0))
#return channel 0, which is blue channel
img.itemset((100, 100, 0), 100)
#set 100,100 channel 0 to 100
#so img[100, 100, 0] become 100 instead of 53
print(img.item(100, 100, 0))
print(img.shape)
#show the img's row and col and channels
print(img.size) 
#row * col = the number of pix
print(img.dtype) 
#date type uint8 etc