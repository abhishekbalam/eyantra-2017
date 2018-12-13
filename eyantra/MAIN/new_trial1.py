import cv2
import numpy as np
import rectification1
import astar_test
import matching
import make_grid
import making_new_grids



low_black = 0
high_black = 115

cap = cv2.VideoCapture(1)

ret_no_use,img_no_use = cap.read()
ret_no_use1,img_no_use1 = cap.read()
ret_no_use2,img_no_use2 = cap.read()
ret_no_use3,img_no_use3 = cap.read()
ret_no_use4,img_no_use4 = cap.read()
ret_no_use5,img_no_use5 = cap.read()
ret_no_use6,img_no_use6 = cap.read()
ret_no_use7,img_no_use7 = cap.read()
ret_no_use8,img_no_use8 = cap.read()
ret_no_use9,img_no_use9 = cap.read()
ret_no_use10,img_no_use10 = cap.read()



ret_img,image = cap.read()






x,y,w,h = rectification1.rectify(image)

final_main_image = image[y+10:y+h-10,x+10:x+w-10]

# main_maze,bot_location = make_grid.define_main_grid(final_main_image)

making_new_grids.determination(final_main_image)

# print main_maze,bot_location
cv2.imshow('',image)
# cv2.imshow('1',image)
cv2.waitKey(0)

cv2.destroyAllWindows()