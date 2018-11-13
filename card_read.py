import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

imgorigin = cv.imread('card.jpg')
imggray = cv.cvtColor(imgorigin, cv.COLOR_RGB2GRAY)
#cv.imshow('gray', imggray)

imgname = imggray[120:305, 8:507]   #cut the picture, get the infomation aera
H, W = imgname.shape[0:2]
H = 2*H
W = 2*W
imgname = cv.resize(imgname, (W, H)) #resize two bigger
#cv.imshow('name', imgname)

ret, imgbw = cv.threshold(imgname, 40, 255, cv.THRESH_BINARY)   #get a BW image
#cv.imshow('BW', imgbw)

kernel1 = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))   #kernel to do close, using cross shape to get a better res
kernel2 = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))    #kernel to do erode
imgerode = cv.morphologyEx(imgbw, cv.MORPH_CLOSE, kernel1)   #do close to xiaochu little noise
imgerode = cv.erode(imgerode, kernel2)   #do erode to get a better target
#cv.imshow('erode', imgerode)

image, contours, hierarchy = cv.findContours(imgerode, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  #get contours
cx = []  #list to save gravity point x
cy = []	 #list to save gravity point y
targetcontours = []  #list to save target contours

for i in range(len(contours)):  #find in all contours
	x, y, w, h = cv.boundingRect(contours[i])  #make a bounding rectangle
	if w > 20 and w <100:   #which is the target size
		rect = cv.rectangle(imgname, (x, y), (x+w, y+h), (0, 255, 0), 2)  #draw bounding rectangle
		M = cv.moments(contours[i])   #get ju of contours
		cx.append(int(M['m10']/M['m00']))  #add gravity point x to cx
		cy.append(int(M['m01']/M['m00']))  #add gravity point y to cy
		targetcontours.append(contours[i]) #saving target contours


# plt.imshow(imgname, cmap = 'gray')
# plt.show()
#print(w, h, cx, cy)
newx = sorted(cx)  #sort cx from small to big
#print(newx)
newy = []   #saving sorted y

for i in range(len(targetcontours)):
	for n in range(len(targetcontours)):
		M = cv.moments(targetcontours[n])
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		if newx[i] == cx:
			newy.append(cy)   #sort cy into newy
			break

#print(newy)

for j in range(len(newx)):
	if newy[j] > 140 and newy[j] <= 170:
		print('0', end=" ")
	if newy[j] > 170 and newy[j] <= 190:
		print('1', end=" ")
	if newy[j] > 190 and newy[j] <= 210:
		print('2', end=" ")
	if newy[j] > 210 and newy[j] <= 230:
		print('3', end=" ")
	if newy[j] > 230 and newy[j] <= 250:
		print('4', end=" ")					
	if newy[j] > 250 and newy[j] <= 270:
		print('5', end=" ")
	if newy[j] > 270 and newy[j] <= 290:
		print('6', end=" ")
	if newy[j] > 290 and newy[j] <= 310:
		print('7', end=" ")
	if newy[j] > 310 and newy[j] <= 340:
		print('8', end=" ")
	if newy[j] > 340 and newy[j] <= 350:
		print('9', end=" ")	

cv.imshow('winname', imgname)
cv.waitKey(0)
cv.destroyAllWindows()