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
	i_bot = 'no'
	j_bot = 'no'
	bot_location = 0
	average_color_tup = []
	gray_init_image = cv2.cvtColor(BGR_image,cv2.COLOR_BGR2GRAY)
	gray_image = cv2.inRange(gray_init_image,64,135)
	cv2.imshow('100',gray_image)
	
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
					average_color_tup.append(average_color)
					if (average_color > 70 and average_color < 90):
						i_bot = i
						j_bot = j
			else :
				cell_h = h/6
				cell_w = w/9
				new_image = gray_image[j*cell_h:j*cell_h+cell_h,i*cell_w:i*cell_w+cell_w]
				average_color_per_row = np.average(new_image, axis=0)
				average_color = np.average(average_color_per_row, axis=0)
				average_color = np.uint8(average_color)
				average_color_tup.append(average_color)
				if (average_color > 70 and average_color < 90):
					i_bot = i
					j_bot = j


	m = max(average_color_tup)

	for j in range(6):
		for i in range(9):
			if j == 0 or j == 5 :
				cell_h = (h/6)-10
				if i == 0 or i == 8 :
					cell_w = (w/9)-10
					if w-i*cell_w > cell_w and h-j*cell_h > cell_h :
						new_image = gray_image[j*cell_h:j*cell_h+cell_h,i*cell_w:i*cell_w+cell_w]
					elif w-i*cell_w < cell_w and h-j*cell_h < cell_h :
						new_image = gray_image[j*cell_h:h,i*cell_w:w]
					else :
						new_image = 0
					average_color_per_row = np.average(new_image, axis=0)
					average_color = np.average(average_color_per_row, axis=0)
					average_color = np.uint8(average_color)
					average_color_tup.append(average_color)			

					# cv2.rectangle(gray_image,(10+i*cell_w,10+j*cell_h),(i*cell_w+cell_w-10,i*cell_w+cell_w-10),(255,255,255),2)
					print 'for',i,j,'=',average_color
					if (( 0 < average_color) and i<8 and j<5):
						main_grid[j][i] = 1

					elif ((10 <= average_color) and i == 8 and j == 5):
						main_grid[j][i] = 1

			else :
				cell_w = w/9
				cell_h = h/6
				if w-i*cell_w > cell_w and h-j*cell_h > cell_h :
					new_image = gray_image[j*cell_h:j*cell_h+cell_h,i*cell_w:i*cell_w+cell_w]
				elif w-i*cell_w < cell_w and h-j*cell_h < cell_h :
					new_image = gray_image[j*cell_h:h,i*cell_w:w]
				else :
					new_image = 0
				average_color_per_row = np.average(new_image, axis=0)
				average_color = np.average(average_color_per_row, axis=0)
				average_color = np.uint8(average_color)
				average_color_tup.append(average_color)			

				cv2.rectangle(gray_image,(i*cell_w,j*cell_h),(i*cell_w+cell_w,i*cell_w+cell_w),(255,255,255),2)
				print 'for',i,j,'=',average_color
				if (( 0 < average_color) and i<8 and j<5):
					main_grid[j][i] = 1

				elif ((10 <= average_color) and i == 8 and j == 5):
					main_grid[j][i] = 1				


	bot_location = (i_bot,j_bot)
	if ((5+8) > i_bot+j_bot):

		main_grid[j_bot][i_bot] = 0

	cv2.imshow('5',gray_image)

	upgrade_grid(main_grid,door_area)
	return main_grid,bot_location

# def define_bot_location(BGR_image,main_grid,door_area):

	# low_toup =33
	# high_toup =49
	# bot_location = 0
	# k = BGR_image.shape
	# w = k[1]
	# h = k[0]
	# cell_w = w/9
	# cell_h = h/6
	# gray_init_image = cv2.cvtColor(BGR_image,cv2.COLOR_BGR2GRAY)
	# gray_image = cv2.inRange(gray_init_image,80,135)
	# for j in range(6):
	# 	for i in range(9):
	# 		new_image = gray_image[j*cell_h:j*cell_h+cell_h,i*cell_w:i*cell_w+cell_w]
	# 		average_color_per_row = np.average(new_image, axis=0)
	# 		average_color = np.average(average_color_per_row, axis=0)
	# 		average_color = np.uint8(average_color)
	# 		print 'for',i,j,'=',average_color

	# 		if (average_color <= high_toup and average_color >= low_toup):
	# 			main_grid[j][i] = 0
	# 			bot_location = (i,j)
	# upgrade_grid(main_grid,door_area)
	# return main_grid,bot_location
































