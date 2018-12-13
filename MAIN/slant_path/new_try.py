import cv2
import numpy as np
# import make_grid
# import astar_test
# import matching



low_black = 0
high_black = 115

cap = cv2.VideoCapture(1)

while 1 :

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



# rough_maze = make_grid.define_main_grid(main_image)
# main_maze,bot_location = make_grid.define_bot_location(main_image,rough_maze)

# shortest_path_bot_to_object = []
# shortest_path_bot_to_marker = []
# matching_pairs = matching.divide_and_match(main_image)
# for i in range(len(matching_pairs)):
# 	match = matching_pairs[i]
# 	shortest_path_bot_to_object.append(astar_test.astar(main_maze,bot_location,match[1]))


	# cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
# print n,index
	cv2.imshow('',main_image)
	cv2.imshow('1',filtered_black)



	# cv2.imshow('img',img) 
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cv2.waitKey(0)
cv2.destroyAllWindows()
	










