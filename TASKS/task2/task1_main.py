# -*- coding: utf-8 -*-
'''
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*  
*  Author: e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
* ---------------------------------------------------
*  Theme: Launch a Module
*  Filename: task1_main.py
*  Version: 1.0.0  
*  Date: November 11, 2016
*  How to run this file: python task1_main.py
*  Author: e-Yantra Project, Department of Computer Science and Engineering, Indian Institute of Technology Bombay.
* ---------------------------------------------------

* ====================== GENERAL Instruction =======================
* 1. Check for "DO NOT EDIT" tags - make sure you do not change function name of main().
* 2. Return should be board_objects and output_list. Both should be list of tuple 
* 3. Do not keep uncessary print statement, imshow() functions in final submission that you submit
* 4. Do not change the file name
* 5. Your Program will be tested through code test suite designed and graded based on number of test cases passed 
**************************************************************************
'''

import cv2
import numpy as np

# ******* WRITE YOUR FUNCTION, VARIABLES etc HERE


def match(path,mode):
	##############color ranges###########

	lowyell=218
	upyell=234
	lowred=68
	upred=82
	lowblue=19
	upblue=36
	lowgreen=135
	upgreen=165

	###############image reading###########
	img = cv2.imread(path,0)
	imgcolor = cv2.imread(path,1)
	h,w,c=imgcolor.shape
	###############Calculation#############
	index=[]
	index4=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
	index3=[1,2,3,4,5,6,7,8,9]
	if (h*w)==160000 :
		index=index4
		divider=4
	else :
		index=index3
		divider=3

	#######################################
	############listing#####################
	var1=0
	var2=0
	varperi=0
	vararea=0
	col_lst=[]
	shape_lst=[]
	perimeter=[]
	area=[]
	for var1 in range( divider*divider ):
		col_lst.append(var1)
	for var2 in range( divider*divider ):	
		shape_lst.append(var2)
	for varperi in range( divider*divider ):	
		perimeter.append(varperi)
	for vararea in range( divider*divider ):	
		area.append(vararea)


	#######################################	
	###############image creation##########

	##############color filtering##########

	filtyell=cv2.inRange(img,lowyell,upyell)
	filtred=cv2.inRange(img,lowred,upred)
	filtblue=cv2.inRange(img,lowblue,upblue)
	filtgrn=cv2.inRange(img,lowgreen,upgreen)

	#######################################
	##############image processing#########
	#yellow

	i=0
	retyel,threshyel = cv2.threshold(filtyell,127,255,0)
	cntyel,hrcyel = cv2.findContours(threshyel, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	ny=len(cntyel)
	#red
	j=0
	retred,threshred = cv2.threshold(filtred,127,255,0)
	cntred,hrcred = cv2.findContours(threshred, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	nr=len(cntred)
	#blue
	k=0
	retred,threshred = cv2.threshold(filtblue,127,255,0)
	cntblue,hrcblue = cv2.findContours(threshred, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	nb=len(cntblue)
	#green
	l=0
	retred,threshred = cv2.threshold(filtgrn,127,255,0)
	cntgreen,hrcgreen = cv2.findContours(threshred, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	ng=len(cntgreen)
	#######################################
	###########processing############
	
	###YELLOW-------
	for i in range(ny):
		imgyel=np.zeros(img.shape,np.uint8)
		M=cv2.moments(cntyel[i])
		Cx=int(M['m10']/M['m00'])
		Cy=int(M['m01']/M['m00'])
	
		AR=cv2.contourArea(cntyel[i])
		PERI=cv2.arcLength(cntyel[i],True)
		
		epsilon = 0.01*cv2.arcLength(cntyel[i],True)
		approx = cv2.approxPolyDP(cntyel[i],epsilon,True)
		cv2.drawContours(imgyel,approx,-1,255,1)
		cv2.imshow('y-det',imgyel)
		cornersyel = cv2.goodFeaturesToTrack(imgyel, 100, 0.01, 10)
		cornersyel = np.int0(cornersyel)
	
		no_corn=len(cornersyel)
		
		if (no_corn==3):
			geo="Triangle"
		elif (no_corn==4):
			geo="4-sided"
		else :
			geo="Circle"
	
	
	
		a=0
		while a<len(index):
			quo=a/divider
			rem=a%divider
			if (Cx<((rem+1)*(w/divider)) and Cy<((quo+1)*(h/divider))):
				col_lst[a]="yellow"
				shape_lst[a]=geo
				area[a]=AR
				perimeter[a]=PERI
				break
			else :
				a=a+1

	###RED-------
	for j in range(nr):
		imgred=np.zeros(img.shape,np.uint8)
		M=cv2.moments(cntred[j])
		Cx=int(M['m10']/M['m00'])
		Cy=int(M['m01']/M['m00'])
	
		AR=cv2.contourArea(cntred[j])
		PERI=cv2.arcLength(cntred[j],True)
	
		epsilon = 0.01*cv2.arcLength(cntred[j],True)
		approx = cv2.approxPolyDP(cntred[j],epsilon,True)
		cv2.drawContours(imgred,approx,-1,255,1)
		cv2.imshow('r-det',imgred)
		cornersred = cv2.goodFeaturesToTrack(imgred, 100, 0.01, 10)
		cornersred = np.int0(cornersred)
	
		no_corn=len(cornersred)
	
		if (no_corn==3):
			geo="Triangle"
		elif (no_corn==4):
			geo="4-sided"
		else :
			geo="Circle"
	
	
	
		a=0
		while a<len(index):
			quo=a/divider
			rem=a%divider
			if (Cx<((rem+1)*(w/divider)) and Cy<((quo+1)*(h/divider))):
				col_lst[a]="red"
				area[a]=AR
				perimeter[a]=PERI
				shape_lst[a]=geo
				break
			else :
				a=a+1

	###BLUE-------
	for k in range(nb):
		imgblue=np.zeros(img.shape,np.uint8)
		M=cv2.moments(cntblue[k])
		Cx=int(M['m10']/M['m00'])
		Cy=int(M['m01']/M['m00'])
	
		AR=cv2.contourArea(cntblue[k])
		PERI=cv2.arcLength(cntblue[k],True)
	
		epsilon = 0.01*cv2.arcLength(cntblue[k],True)
		approx = cv2.approxPolyDP(cntblue[k],epsilon,True)
		cv2.drawContours(imgblue,approx,-1,255,1)
		cv2.imshow('b-det',imgblue)
		corners = cv2.goodFeaturesToTrack(imgblue, 100, 0.01, 10)
		corners = np.int0(corners)
	
		no_corn=len(corners)
	
		if (no_corn==3):
			geo="Triangle"
		elif (no_corn==4):
			geo="4-sided"
		else :
			geo="Circle"
	
	
	
		a=0
		while a<len(index):
			quo=a/divider
			rem=a%divider
			if (Cx<((rem+1)*(w/divider)) and Cy<((quo+1)*(h/divider))):
				col_lst[a]="blue"
				area[a]=AR
				perimeter[a]=PERI
				shape_lst[a]=geo
				break
			else :
				a=a+1


	###green-------
	for l in range(ng):
		imggreen=np.zeros(img.shape,np.uint8)
		M=cv2.moments(cntgreen[l])
		Cx=int(M['m10']/M['m00'])
		Cy=int(M['m01']/M['m00'])
	
		AR=cv2.contourArea(cntgreen[l])
		PERI=cv2.arcLength(cntgreen[l],True)
	
		epsilon = 0.01*cv2.arcLength(cntgreen[l],True)
		approx = cv2.approxPolyDP(cntgreen[l],epsilon,True)
		cv2.drawContours(imggreen,approx,-1,255,1)
	
		cornersgreen = cv2.goodFeaturesToTrack(imggreen, 100, 0.01, 10)
		cornersgreen = np.int0(cornersgreen)
		cv2.imshow("green",imggreen)
		no_corn=len(cornersgreen)
	
		if (no_corn==3):
			geo="Triangle"
		elif (no_corn==4):
			geo= "4-sided"
		else :
			geo="Circle"
	
		a=0
		while a<len(index):
			quo=a/divider
			rem=a%divider
			if (Cx<((rem+1)*(w/divider)) and Cy<((quo+1)*(h/divider))):
				col_lst[a]="green"
				area[a]=AR
				perimeter[a]=PERI
				shape_lst[a]=geo
				break
			else :
				a=a+1

	finalans=[]
	finalans2=[]
	
	for bc in range(len(index)):
		finalans.append([index[bc],col_lst[bc],shape_lst[bc]])
		finalans[bc]=tuple(finalans[bc])


	for bc in range(len(index)):
		finalans2.append([col_lst[bc],shape_lst[bc],area[bc],perimeter[bc]])
		finalans2[bc]=tuple(finalans2[bc])
		
	if (mode==0):
		return finalans
	else:
		return col_lst,shape_lst,area,perimeter,index


def generate_common(one,two):

	oneCol,oneShape,oneArea,onePeri,oneInd = match(one,1);
	twoCol,twoShape,twoArea,twoPeri,twoInd = match(two,1);

	B1=0
	C2=0
	output=[]
	temp=0
	for B1 in range(len(oneInd)):
		for C2 in range(len(twoInd)):

			if(oneCol[B1]==twoCol[C2] and oneShape[B1]==twoShape[C2] and onePeri[B1]==twoPeri[C2] and oneArea[B1]==twoArea[C2]):
				output.append((B1+1,C2+1))
				temp=0
				break;	
			else:
				temp=1

		if(temp == 1):
			output.append((B1+1,0))
	
	return output



def main(board_filepath, container_filepath):
	'''
This function is the main program which takes image of game-board and
container as argument. Team is expected to insert their part of code as
required to solve the given task (function calls etc).

***DO NOT EDIT THE FUNCTION NAME. Leave it as main****
Function name: main()

******DO NOT EDIT name of these argument*******
Input argument: board_filepath and container_filepath.

Return: 
1 - List of tuples which is the expected final output. See Task1_Description for detail. 
2 - List of tuples for objects on board. See Task1_Description for detail. 
	''' 
	

	board_objects = []		# List to store output of board -- DO NOT CHANGE VARIABLE NAME
	output_list = []		# List to store final output 	-- DO NOT CHANGE VARIABLE NAME
	



	##### WRITE YOUR CODE HERE - STARTS

	# cv2.imshow("board_filepath - press Esc to close",cv2.imread(board_filepath))			- For check - remove
	# cv2.imshow("container_filepath - press Esc to close",cv2.imread(container_filepath))

	board_objects = match(board_filepath,0)
	output_list = generate_common(board_filepath,container_filepath)


	#print board_objects
	#print output_list
	#cv2.waitKey(0)
	cv2.destroyAllWindows()    

	# #### NO EDIT AFTER THIS

# DO NOT EDIT
# return Expected output, which is a list of tuples. See Task1_Description for detail.
	return board_objects, output_list	



'''
Below part of program will run when ever this file (task1_main.py) is run directly from terminal/Idle prompt.

'''
if __name__ == '__main__':
    

	board_filepath = "test_images/board_5.jpg"    			# change filename of board provided to you 
	container_filepath = "test_images/container_1.jpg"		# change filename of container as required for testing

	main(board_filepath,container_filepath)

	cv2.waitKey(0)
	cv2.destroyAllWindows()    
