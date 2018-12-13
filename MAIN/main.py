import cv2
import numpy as np
import make_grid
import astar_test
import matching



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




gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

new_image = np.zeros(image.shape,np.uint8)

filtered_black = cv2.inRange(gray,low_black,high_black)

ret,thresh = cv2.threshold(filtered_black,127,255,0)
cnt,hrc = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


area_cnt = []
n = len(cnt)

for i in range(n):
	area_cnt.append(cv2.contourArea(cnt[i]))

m = max(area_cnt)
for i in range(n):
	if area_cnt[i] == m :
		area_cnt[i] = 0


new_max = max(area_cnt)
for i in range(n):
	if area_cnt[i] == new_max :
		index = i

main_image_contour = cnt[index]

x,y,w,h = cv2.boundingRect(main_image_contour)
main_image = image[y:y+h,x:x+w]



rough_maze,rough_door = make_grid.define_main_grid(main_image)
main_maze,bot_location = make_grid.define_bot_location(main_image,rough_maze,rough_door)

# shortest_path_bot_to_object = []
# shortest_path_bot_to_marker = []
# matching_pairs = matching.divide_and_match(main_image)
# for i in range(len(matching_pairs)):
# 	match = matching_pairs[i]
# 	shortest_path_bot_to_object.append(astar_test.astar(main_maze,bot_location,match[1]))


cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
print main_maze
cv2.imshow('',main_image)
cv2.imshow('1',filtered_black)
cv2.waitKey(0)
cv2.destroyAllWindows()
	










