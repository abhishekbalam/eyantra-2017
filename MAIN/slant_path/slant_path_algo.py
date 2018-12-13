import cv2
import numpy as np
import math

maze = [[0 for i in range(9)]for i in range(6)]


maze[3][3] = 1


def find_slant_path(maze,stpnt,endpnt):
	x1 = stpnt[0]
	y1 = stpnt[1]
	x2 = endpnt[0]
	y2 = endpnt[1]
	i = 0
	j = 0
	slant = False
	m = 0

	dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	int_dist = int(dist)
	if(stpnt[0]+stpnt[1] == endpnt[0]+endpnt[1]) or (stpnt[0]-stpnt[1] == endpnt[0]-endpnt[1]) :
		if x2 > x1 and y2 > y1 :
			while (math.sqrt(((i-x1)**2)+((j-y1)**2)) <= dist) :
				if maze[j][i] == 1 :
					slant = False
					return slant
					break
				else :
					slant = True 
					m = 1 

				i = i+1
				j = j+1
		elif x2 > x1 and y2 < y1 :
			while (math.sqrt(((i-x1)**2)+((j-y1)**2)) <= dist) :
				if maze[j][i] == 1 :
					slant = False
					return slant
					break
				else :
					slant = True 
					m = 2

				i = i+1
				j = j-1
		elif x2 < x1 and y2 < y1 :
			while (math.sqrt(((i-x1)**2)+((j-y1)**2)) >= dist) :
				if maze[j][i] == 1 :
					slant = False
					return slant
					break
				else :
					slant = True 
					m = 3

				i = i+1
				j = j+1

		elif x2 < x1 and y2 > y1 :
			while (math.sqrt(((i-x1)**2)+((j-y1)**2)) <= dist) :
				if maze[j][i] == 1 :
					slant = False
					return slant
					break
				else :
					slant = True 
					m = 4

				i = i-1
				j = j+1	



	return slant,m



def generate_path(stpnt,endpnt,mode,slant):
	x1 = stpnt[0]
	y1 = stpnt[1]
	x2 = endpnt[0]
	y2 = endpnt[1]
	dist = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
	i = 0
	j = 0
	k = 0
	l = 0
	resultant_path = []
	if slant:
		if mode == 1 :
			k = x1 + i
			l = y1 + j

			while (math.sqrt(((k-x1)**2)+((l-y1)**2)) <= dist) :
				
				resultant_path.append((x1+i,y1+j))
				if x1+i == x2 and y1+i == y2 :
					break

				i = i+1
				k = x1 + i
				j = j+1
				l = y1 + j

		elif mode == 2 :
			k = x1 + i
			l = y1 + j
			while (math.hypot(k-x1,l-y1) <= dist) :
				
				resultant_path.append((x1+i,y1+j))
				if x1+i == x2 and y1+i == y2 :
					break
				
				i = i+1
				k = x1 + i
				j = j-1
				l = y1 + j 
				


		elif mode == 3 :
			k = x1 + i
			l = y1 + j
			while (math.sqrt(((k-x1)**2)+((l-y1)**2)) <= dist) :
				resultant_path.append((x1+i,y1+j))
				if x1+i == x2 and y1+i == y2 :
					break


				i = i-1
				k = x1 + i
				j = j-1
				l =y1 + j

		elif mode == 4 :
			k = x1 + i
			l = y1 + j
			while (math.sqrt(((k-x1)**2)+((l-y1)**2)) <= dist) :
				resultant_path.append((x1+i,y1+j))
				if x1+i == x2 and y1+i == y2 :
					break


				i = i-1
				k = x1 + i
				j = j+1
				l = y1 + j


	return resultant_path


start = (4,4)
end = (1,1)


s,method = find_slant_path(maze,start,end)
# final_path = generate_path(start,end,method,s)

print s,method






