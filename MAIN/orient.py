import cv2
import numpy as np
import detectmax_bot as d_b

def orientation(strng):
	img = cv2.imread(strng)
	new_img = np.zeros(img.shape , np.uint8)
	contour = d_b.detect_max_area_contour(strng)


	# epsilon = 0.01*cv2.arcLength(contour,True)
	# approx = cv2.approxPolyDP(contour,epsilon,True)

	x,y,w,h = cv2.boundingRect(contour)
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
	center,status,angle = cv2.minAreaRect(contour)

	x_rot = center[0]
	y_rot = center[1]
	width = status[0]
	height = status[1]

	if 0.9*w == width and 0.9*h == height :
		alligned = True
		if alligned and x_rot > 0.5*img.shape[0] and y_rot == 0.5*img.shape[1] :
			return 'right'
		elif alligned and x_rot < 0.5*img.shape[0] and y_rot == 0.5*img.shape[1] :
			return 'left'
		elif alligned and x_rot == 0.5*img.shape[0] and y_rot < 0.5*img.shape[1] :
			return 'up'
		elif alligned and x_rot == 0.5*img.shape[0] and y_rot > 0.5*img.shape[1] :
			return 'down'










