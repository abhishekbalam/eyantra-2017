import cv2
import numpy as np
import rectification1



cap =cv2.VideoCapture(1)

while 1 :
	ret,imge = cap.read()
	# img = cv2.cvtColor(imge,cv2.COLOR_BGR2GRAY)



	# x1,y1,w1,h1 = rectification1.rectify(imge)
	# cv2.rectangle(imge,(x1,y1),(x1+w1,y1+h1),(0,0,255),2)
	# x2 = x1+10
	# y2 = y1 +10
	# A = y1+h1-5
	# B = x1+w1-5
	# m_img = imge[y2:A,x2:B]

	# x2,y2,w2,h2 = rectification1.rectify(m_img)

	# main_img = m_img[y2:y2+h2,x2:x2+w2]



	cv2.imshow('',imge)
	# print x1 , x1
	# print y1,y2
	# print w1,w2
	# print h1,h2

	# cv2.imshow('img',m_img)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
