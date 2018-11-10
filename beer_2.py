import cv2 as cv
import numpy as np

img = cv.imread('./BEER/Bad/4.tif')
H, W = img.shape[0:2]
#get size of img
X = int(H/10)
Y = int(W/10)
num = 0
#resize factor
kerneldilate = cv.getStructuringElement(cv.MORPH_RECT,(11, 11))
kernelerode = cv.getStructuringElement(cv.MORPH_RECT,(9, 9))
kernel2 = np.ones((5, 5), np.float32)/25
kernel3 = np.ones((7, 7), np.float32)/49
#make a kernel to do dilate

imgrgb = cv.resize(img, (X, Y))
#resize image which is too big
imggray = cv.cvtColor(imgrgb, cv.COLOR_BGR2GRAY)
cv.imshow('gray', imggray)

clahe = cv.createCLAHE(clipLimit=8.0, tileGridSize=(50,50))
cl1 = clahe.apply(imggray)
cv.imshow('clahe', cl1)

imgfilter = cv.bilateralFilter(cl1, 35, 47, 13)
cv.imshow('filter', imgfilter)

ret, thresh = cv.threshold(imgfilter, 90, 255, cv.THRESH_BINARY)
thresh = cv.dilate(thresh, kerneldilate)
cv.imshow('the1', thresh)
thresh = cv.filter2D(thresh, -1, kernel2)
cv.imshow('avg', thresh)

ret, thresh = cv.threshold(thresh, 100, 255, cv.THRESH_BINARY)
thresh = cv.dilate(thresh, kerneldilate)
cv.imshow('the2', thresh)

thresh = cv.filter2D(thresh, -1, kernel2)
cv.imshow('avg2', thresh)

ret, thresh = cv.threshold(thresh, 100, 255, cv.THRESH_BINARY)
cv.imshow('the3', thresh)
# thresh = cv.erode(thresh, kernelerode)


# dilate = cv.dilate(thresh, kerneldilate)
# cv.imshow('res', dilate)

image, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

for i in range(len(contours)):
	(x,y),radius = cv.minEnclosingCircle(contours[i])
	center = (int(x),int(y))
	radius = int(radius)
	# cir = cv.circle(dilate,center,radius,(0,0,0),2)
	print(radius)
	if radius<60 :
		num += 1
cv.putText(thresh, 'beer number is ' + str(num), (50, 50), cv.FONT_HERSHEY_SIMPLEX, 0.8, 255, 2, cv.LINE_AA)
cv.imshow('final', thresh)

print("the num of beers is " + str(num))
cv.waitKey(0)
cv.destroyAllWindows()
