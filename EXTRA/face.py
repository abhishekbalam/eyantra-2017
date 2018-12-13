import cv2
import numpy as np

cap = cv2.VideoCapture(1)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


while 1:
	ret,img=cap.read()
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces :
		cv2.circle(img,(x+(h/2),y+(w/2)),((w+h)/2),(255,255,0),2)
		roi_gray = gray[y:y+h,x:x+w]
		roi_color = img[y:y+h,x:x+w]
	cv2.imshow('',img)
	k = cv2.waitKey(30) & 0xff
	if k == 27 :
		break

	
cap.release()
cv2.destroyAllWindows()