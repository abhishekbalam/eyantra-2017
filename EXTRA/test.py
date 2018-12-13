import cv2
import numpy as np
import time

image = cv2.imread('output.png')
img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


average_color_per_row = np.average(img, axis=0)
average_color = np.average(average_color_per_row, axis=0)
average_color = np.uint8(average_color)



print average_color
cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


