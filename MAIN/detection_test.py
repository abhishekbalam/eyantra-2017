import cv2
import numpy as np
import detectmax_bot as d_b


strng = 'new2.jpg'
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

if w == width && h == height :
	alligned = True
	if alligned && x_rot > 0.5*img.shape[0] && y_rot < 0.6*img.shape[1] :
		return 'right'
	elif alligned && x_rot < 0.5*img.shape[]





# cv2.drawContours(new_img,approx,-1,255,1)
cv2.imshow('',img)

cv2.waitKey(0)
cv2.destroyAllWindows()




