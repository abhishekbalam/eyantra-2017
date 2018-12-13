import numpy as np
import cv2

cap = cv2.VideoCapture(1)
cap_2 = cv2.VideoCapture(0)


while(True):
	ret, frame = cap.read()
	ret_2,frame_2 = cap_2.read()

    # Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray_2 = cv2.cvtColor(frame_2, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
	cv2.imshow('',gray)
	cv2.imshow('1',gray_2)
	k = cv2.waitKey(30) & 0xff
	if k == 27 :
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
