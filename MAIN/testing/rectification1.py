import cv2
import numpy as np



def rectify(image):
	low =0
	high=115
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	new_image = np.zeros(image.shape,np.uint8)
	filtered_black = cv2.inRange(gray,low,high)
	ret,thresh = cv2.threshold(filtered_black,127,255,0)
	cnt,hrc = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	n = len(cnt)
	area=[]
	for i in range(n) :
		area.append(cv2.contourArea(cnt[i]))
	m = max(area)
	
	for i in range(n):
		if (area[i]==m):
			area[i]=0
	new_m = max(area)
	for i in range(n):
		if (area[i]==new_m) :
			index = i
	main_contour = cnt[index]

	x,y,w,h = cv2.boundingRect(main_contour)

	return x,y,w,h






