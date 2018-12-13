import cv2
import numpy as np 

def detect_max_area_contour(s):
	low_t = (200,200,200)
	high_t = (255,255,255)
	img = cv2.imread(s)

	new_img = cv2.inRange(img,low_t,high_t)
	# cv2.imshow('1',cv2.imread('new2.jpg'))
	# cv2.imshow('',new_img)

	ret,thresh = cv2.threshold(new_img,127,255,0)
	cnt,hrc = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	# blank_img = np.zeros(img.shape,np.uint8 )
	n = len(cnt)
	area = []
	for i in range(n):
		area.append(cv2.contourArea(cnt[i]))

	m = max(area)


	for i in range(n):
		if cv2.contourArea(cnt[i]) == m :
			rec = i 

	return cnt[rec]



