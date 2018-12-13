import cv2
import numpy as np

face = cv2.imread('pCZfV.png')

blank = np.zeros(face.shape , np.uint8)

dst = cv2.addWeighted(face,1,blank,1,0)

cv2.imshow('',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()