import cv2
import numpy as np


def upgrade_grid(main_grid,door_area):
	for j in range(6) :
		for i in range(9):
			if i == 0 :
				door_area.append(main_grid[j][i])



def define_main_grid(BGR_image):

	door_area = []

	main_grid = [[0 for i in range(9)]for i in range(6)]



	k = BGR_image.shape
	w = k[1]+20
	h = k[0]+20
	gray_init_image = cv2.cvtColor(BGR_image,cv2.COLOR_BGR2GRAY)
	gray_image = cv2.inRange(gray_init_image,80,135)
	
	for j in range(6):
		for i in range(9):
			if j == 0 or j == 5 :
				cell_h = (h/6)-10
				if i == 0 or i == 8 :
					cell_w = (w/9)-10

					new_image = gray_image[j*cell_h:j*cell_h+cell_h,i*cell_w:i*cell_w+cell_w]
					average_color_per_row = np.average(new_image, axis=0)
					average_color = np.average(average_color_per_row, axis=0)
					average_color = np.uint8(average_color)
					cv2.rectangle(BGR_image,(i*cell_w,j*cell_h),(i*cell_w+cell_w,i*cell_w+cell_w),(0,0,255),2)
					# print 'for',i,j,'=',average_color
					if ((4.9 <= average_color) and i<8 and j<5):
						main_grid[j][i] = 1

					elif ((25 <= average_color) and i == 8 and j == 5):
						main_grid[j][i] = 1

			else :
				cell_w = w/9
				cell_h = h/6
				new_image = gray_image[j*cell_h:j*cell_h+cell_h,i*cell_w:i*cell_w+cell_w]
				average_color_per_row = np.average(new_image, axis=0)
				average_color = np.average(average_color_per_row, axis=0)
				average_color = np.uint8(average_color)
				cv2.rectangle(BGR_image,(i*cell_w,j*cell_h),(i*cell_w+cell_w,i*cell_w+cell_w),(0,0,255),2)
				# print 'for',i,j,'=',average_color
				if ((4.9 <= average_color) and i<8 and j<5):
					main_grid[j][i] = 1

				elif ((25 <= average_color) and i == 8 and j == 5):
					main_grid[j][i] = 1
				

	cv2.imshow('5',gray_image)
	upgrade_grid(main_grid,door_area)
	return main_grid,door_area

def define_bot_location(BGR_image,main_grid,door_area):

	low_toup =33
	high_toup =49
	bot_location = 0
	k = BGR_image.shape
	w = k[0]
	h = k[1]
	cell_w = w/9
	cell_h = h/6
	gray_init_image = cv2.cvtColor(BGR_image,cv2.COLOR_BGR2GRAY)
	gray_image = cv2.cvtColor(BGR_image,cv2.COLOR_BGR2GRAY)
	for j in range(6):
		for i in range(9):
			new_image = gray_image[j*cell_h:j*cell_h+cell_h,i*cell_w:i*cell_w+cell_w]
			average_color_per_row = np.average(new_image, axis=0)
			average_color = np.average(average_color_per_row, axis=0)
			average_color = np.uint8(average_color)

			if (average_color <= high_toup and average_color >= low_toup):
				main_grid[j][i] = 0
				bot_location = (i,j)


	upgrade_grid(main_grid,door_area)
	return main_grid,bot_location
































