import cv2
import numpy as np


def determination(image):

	b_high = (230,150,100)
	b_low = (190,110,80)
	g_high = (200,150,60)
	g_low = (100,120,40)
	r_high =(90,100,250)
	r_low = (70,80,180)


	grid = [[0 for i in range(9)]for i in range(6)]

	k = image.shape
	w = k[0]+20
	h = k[1]+20

	b_filt = cv2.inRange(image,b_low,b_high)
	g_filt = cv2.inRange(image,g_low,g_high)
	r_filt = cv2.inRange(image,r_low,r_high)

	for j in range(6):
		for i in range(9):
			if j == 0 or j == 5 :
				c_h = (h/6)-10
				if i == 0 or i == 9 :
					c_w = (w/9)-10

					b_cell = b_filt[j*c_h:j*c_h+c_h,i*c_w:i*c_w+c_w]
					g_cell = g_filt[j*c_h:j*c_h+c_h,i*c_w:i*c_w+c_w]
					r_cell = r_filt[j*c_h:j*c_h+c_h,i*c_w:i*c_w+c_w]
					average_color_per_row_b = np.average(b_cell, axis=0)
					average_color_b = np.average(average_color_per_row_b, axis=0)
					average_color_b = np.uint8(average_color_b)

					average_color_per_row_g = np.average(g_cell, axis=0)
					average_color_g = np.average(average_color_per_row_g, axis=0)
					average_color_g = np.uint8(average_color_g)


					average_color_per_row_r = np.average(r_cell, axis=0)
					average_color_r = np.average(average_color_per_row_r, axis=0)
					average_color_r = np.uint8(average_color_r)	

					if (average_color_r > 0 or average_color_g > 0 or average_color_b > 0):
						grid[j][i] = 1

					else :
						grid[j][i] = 0 


			else :

				c_w = w/9
				c_h = h/6

				b_cell = b_filt[j*c_h:j*c_h+c_h,i*c_w:i*c_w+c_w]
				g_cell = g_filt[j*c_h:j*c_h+c_h,i*c_w:i*c_w+c_w]
				r_cell = r_filt[j*c_h:j*c_h+c_h,i*c_w:i*c_w+c_w]
				average_color_per_row_b = np.average(b_cell, axis=0)
				average_color_b = np.average(average_color_per_row_b, axis=0)
				average_color_b = np.uint8(average_color_b)

				average_color_per_row_g = np.average(g_cell, axis=0)
				average_color_g = np.average(average_color_per_row_g, axis=0)
				average_color_g = np.uint8(average_color_g)


				average_color_per_row_r = np.average(r_cell, axis=0)
				average_color_r = np.average(average_color_per_row_r, axis=0)
				average_color_r = np.uint8(average_color_r)	

				if (average_color_r > 0 or average_color_g > 0 or average_color_b > 0):
					grid[j][i] = 1

				else :
					grid[j][i] = 0 

					


					

	print grid
	cv2.imshow('1',r_filt)
	cv2.imshow('2',g_filt)	
	cv2.imshow('3',b_filt)
	cv2.imshow('og',image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
