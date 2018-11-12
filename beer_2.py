#this version can do better
#80% current rant of good view
#
import cv2 as cv
import numpy as np

for n in range(0, 22):
	e1 = cv.getTickCount()
	img = cv.imread('./BEER/Bad/'+str(n)+'.tif')
	H, W = img.shape[0:2]  #get size of image
	X = int(H/10)
	Y = int(W/10)   #resize
	num = 0

	kerneldilate = cv.getStructuringElement(cv.MORPH_RECT,(11, 11))  #kernel to do dilate
	kernelerode = cv.getStructuringElement(cv.MORPH_RECT,(9, 9))     #kernel to do erode
	kernel2 = np.ones((5, 5), np.float32)/25			#average kernel 1
	kernel3 = np.ones((7, 7), np.float32)/49			#average kernel 2

	imgrgb = cv.resize(img, (X, Y))  #resize image  
	imggray = cv.cvtColor(imgrgb, cv.COLOR_BGR2GRAY)  #convert rgb image into gray image
	#cv.imshow('gray', imggray)

	clahe = cv.createCLAHE(clipLimit = 8.0, tileGridSize = (50,50))  #do the CLAHE (ju bu zhi fang tu jun heng)
	#gray > 8, will be cut and devert to others
	cl1 = clahe.apply(imggray)
	#cv.imshow('clahe', cl1)

	imgfilter = cv.bilateralFilter(cl1, 35, 47, 13)  #do a bilateral filter to save edge and pass noise
	#cv.imshow('filter', imgfilter)

	ret, thresh = cv.threshold(imgfilter, 90, 255, cv.THRESH_BINARY)  #do a threshold, to get a BW pic
	thresh = cv.dilate(thresh, kerneldilate)  #do dilate to mask noise which is 0(peng zhang)
	#cv.imshow('the1', thresh)
	thresh = cv.filter2D(thresh, -1, kernel2) #do average filter in order to get a better pir(less noise)
	#cv.imshow('avg', thresh)

	ret, thresh = cv.threshold(thresh, 100, 255, cv.THRESH_BINARY) #do threshold again, but this time noise is less
	thresh = cv.dilate(thresh, kerneldilate)  #dilate again to get a smoother pic
	#cv.imshow('the2', thresh)

	thresh = cv.filter2D(thresh, -1, kernel2) #average filter again to make noise less
	#cv.imshow('avg2', thresh)
	ret, thresh = cv.threshold(thresh, 100, 255, cv.THRESH_BINARY) #threshold three times to get better
	#cv.imshow('the3', thresh)

	image, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	#find contours
	#print(len(contours))

	for i in range(len(contours)):
		(x,y),radius = cv.minEnclosingCircle(contours[i])  #make a mini enclosing circle of contours
		center = (int(x),int(y))  #circle's origin point
		radius = int(radius)  #radius
		#print(radius)
		if radius < 40 :  #which is our target
			num += 1    #sum of target
			x, y, w, h = cv.boundingRect(contours[i])  #make a bound rectangle, (x, y)is youshangjiao
			rec = cv.rectangle(imgrgb, (x, y), (x + w, y + h), (209, 206, 0), 1) #draw bound rectangle on the origin image


	e2 = cv.getTickCount()
	time = (e2 - e1)/cv.getTickFrequency()  #stop timing
	time = round(time, 4)

	cv.putText(imgrgb, 'beer number is ' + str(num), (50, 350), cv.FONT_HERSHEY_SIMPLEX, 0.8, (106, 106, 255), 2, cv.LINE_AA)
	cv.putText(imgrgb, 'time: ' + str(time) + 's', (50, 400), cv.FONT_HERSHEY_SIMPLEX, 0.8, (214, 112, 218), 2, cv.LINE_AA)
	cv.imshow('final'+str(n), imgrgb)

	#print("the num of beers is " + str(num))
cv.waitKey(0)
cv.destroyAllWindows()
