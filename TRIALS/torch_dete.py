import cv2 
import numpy as np 


cap = cv2.VideoCapture(0)
low_buff = 230
high_buff = 255
while 1:
	ret, trial = cap.read()
	img = cv2.cvtColor(trial, cv2.COLOR_BGR2GRAY)
	
	
	filt_white=cv2.inRange(img,low_buff,high_buff)


	ret_white,thresh_white = cv2.threshold(filt_white,127,255,0)
	cnt_white,hrc_white = cv2.findContours(thresh_white, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	area = []
	lar_ar = 0
	n = 0
	for i in range(len(cnt_white)):
		AR=cv2.contourArea(cnt_white[i])
		area.append(AR)

	for i in range(len(area)):
		if lar_ar < area[i]:
			lar_ar = area[i]
			n = i
		
	if n != 0:
		img_white=np.zeros(img.shape,np.uint8)
		M=cv2.moments(cnt_white[n])
		Cx=int(M['m10']/M['m00'])
		Cy=int(M['m01']/M['m00'])

		# if Cx > 0.7*w:
		# 	print 'BHOSDIVALA'
		cv2.circle(trial,(Cx,Cy), 63, (0,0,255), 2)

		print (Cx,Cy)

	cv2.imshow('white',trial)
	# cv2.imshow('white',filt_white)


	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break


cap.release()


cv2.destroyAllWindows()
