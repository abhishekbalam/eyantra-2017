import cv2
import numpy as np
# import make_grid
# import astar_test
# import matching



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
xinit_main_image = image[y:y+h+6,x:x+w+6]
init_main_image = cv2.cvtColor(xinit_main_image,cv2.COLOR_BGR2GRAY)

main_image = cv2.inRange(init_main_image,low_black,high_black+5)
new_main_blank = np.zeros(main_image.shape,np.uint8)

ret_new,thresh_new = cv2.threshold(main_image,127,255,0)
cnt_new,hrc_new = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


area_cnt_new = []
n_new = len(cnt_new)

for i in range(n_new):
	area_cnt_new.append(cv2.contourArea(cnt_new[i]))

m_new = max(area_cnt_new)
for i in range(n_new):
	if area_cnt_new[i] == m_new :
		area_cnt_new[i] = 0


new_max_new = max(area_cnt_new)
for i in range(n_new):
	if area_cnt_new[i] == new_max_new :
		index_new = i

main_image_contour_new = cnt_new[index_new]

x_new,y_new,w_new,h_new = cv2.boundingRect(main_image_contour_new)

cv2.drawContours(main_image, main_image_contour_new, -1, (0,255,0), 3)
final_main_image = xinit_main_image[y_new:y_new+h_new,x_new:x_new+w_new]

print cnt,cnt_new

cv2.imshow('',main_image_contour_new)
cv2.waitKey(0)
cv2.destroyAllWindows()