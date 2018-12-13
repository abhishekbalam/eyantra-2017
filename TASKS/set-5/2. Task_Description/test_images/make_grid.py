import cv2
import numpy as np


def upgrade_grid(main_grid,door_area):
	for j in range(6) :
		for i in range(9):
			if i == 0 :
				door_area.append(main_grid[j][i])



def define_main_grid(BGR_image):

	door_area = []

	main_grid = [[0 for i in range(10)]for i in range(10)]



	k = BGR_image.shape
	w = k[0]
	h = k[1]
	cell_w = w/10
	cell_h = h/10
	gray_image = cv2.cvtColor(BGR_image,cv2.COLOR_BGR2GRAY)
	for j in range(10):
		for i in range(10):
			new_image = gray_image[j*cell_h:j*cell_h+cell_h,i*cell_w:i*cell_w+cell_w]
			average_color_per_row = np.average(new_image, axis=0)
			average_color = np.average(average_color_per_row, axis=0)
			average_color = np.uint8(average_color)
			if (240 >= average_color):
				main_grid[j][i] = 1


	upgrade_grid(main_grid,door_area)
	return main_grid

def define_bot_location(BGR_image,main_grid):

	low_toup =10
	high_toup =100

	k = BGR_image.shape
	w = k[0]
	h = k[1]
	cell_w = w/9
	cell_h = h/6
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


string = 'test_image1.jpg'
image = cv2.imread(string)
maze = define_main_grid(image)
print maze































