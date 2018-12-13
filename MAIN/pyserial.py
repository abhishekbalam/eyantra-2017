import serial
import cv2 
import numpy as np

def direction(path,orientation):
	direction = []
	for j in range(len(path)):
		if(j<(len(path)-1)):
			k=j+1
			print "(",path[j][0],",",path[j][1],")->(",path[k][0],",",path[k][1],")"
		if(path[j][0]==path[k][0]):
			if(path[j][1]==(path[k][1]-1)):
				print("right\n")
				direction.append(1)
			elif(path[j][1]==(path[k][1]+1)):
				print("left\n")
				direction.append(2)
		elif(path[j][1]==path[k][1]):
			if(path[j][0]==path[k][0]-1):
				print("down\n")
				direction.append(3)
			if(path[j][0]==path[k][0]+1):
				print("up\n")
				direction.append(4)
		
	return direction

print(direction([(1,1),(1,2),(2,2),(2,3),(1,3),(1,4)],0))