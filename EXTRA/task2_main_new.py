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
*  Filename: task2_main.py
*  Version: 1.0.0  
*  Date: November 28, 2016
*  How to run this file: python task2_main.py
*  Author: e-Yantra Project, Department of Computer Science and Engineering, Indian Institute of Technology Bombay.
* ---------------------------------------------------

* ====================== GENERAL Instruction =======================
* 1. Check for "DO NOT EDIT" tags - make sure you do not change function name of main().
* 2. Return should be a list named occupied_grids and a dictionary named planned_path.
* 3. Do not keep uncessary print statement, imshow() functions in final submission that you submit
* 4. Do not change the file name
* 5. Your Program will be tested through code test suite designed and graded based on number of test cases passed 
**************************************************************************
'''

# * Team Id : < lm#153 >
# * Author List : < Abhishek Balam, Ameya Mahadik, Bhaskar Kulkarni, Rahul Pikale>
# * Filename: < Task_2 >
# * Theme: < eYRC- Launch a Module >
# * Functions: < Main function:-main(image_filename)
# *              Sub  function:-analyse(img,img1),analyse_main(imag,imag1),sliding_window(image, stepSize, windowSize),astar(m,startp,endp) >
# * Global Variables: < none >
import cv2
import numpy as np

# ******* WRITE YOUR FUNCTION, VARIABLES etc HERE

# 	* Function Name: < main >
# * Input: < image_filename >
# * Output: < occupids grids (list) planned list(dictionary)  >
# * Logic: < takes the image and calls various functions and returns required output >
def main(image_filename):
	'''
This function is the main program which takes image of test_images as argument. 
Team is expected to insert their part of code as required to solve the given 
task (function calls etc).

***DO NOT EDIT THE FUNCTION NAME. Leave it as main****
Function name: main()

******DO NOT EDIT name of these argument*******
Input argument: image_filename

Return:
1 - List of tuples which is the coordinates for occupied grid. See Task2_Description for detail. 
2 - Dictionary with information of path. See Task2_Description for detail.
	'''

	occupied_grids = []		# List to store coordinates of occupied grid -- DO NOT CHANGE VARIABLE NAME
	planned_path = {}		# Dictionary to store information regarding path planning  	-- DO NOT CHANGE VARIABLE NAME
	



	##### WRITE YOUR CODE HERE - STARTS

	# cv2.imshow("board_filepath - press Esc to close",cv2.imread(board_filepath))			- For check - remove
	# cv2.imshow("container_filepath - press Esc to close",cv2.imread(container_filepath))
	'''
	Returns:
	1 - List of tuples which is the coordinates for occupied grid. 
	2 - Dictionary with information of path. 
	'''

# 	* Function Name: <analyse>
# * Input: < img,img1 >
# * Output: < ok with a value of comparison >
# * Logic: <compares the 2 images'contour area and shape and returns the compare value in the form of 1 and 0 >
# * Example Call: < eg. variable_name = analyse(img,img1) >
	def analyse(img,img1):


		ret1,thresh1 = cv2.threshold(img,127,255,0)
		cnt1,hrc1 = cv2.findContours(thresh1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		ret2,thresh2 = cv2.threshold(img1,127,255,0)
		cnt2,hrc2 = cv2.findContours(thresh2, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

		
		imgn=np.zeros(img.shape,np.uint8)
		imgn1=np.zeros(img.shape,np.uint8)

		
		if len(cnt1)!=0 and len(cnt2)!=0:
			A1=cv2.contourArea(cnt1[0])
			A2=cv2.contourArea(cnt2[0])


			eps1 = 0.01*cv2.arcLength(cnt1[0],True)
			eps2 = 0.01*cv2.arcLength(cnt2[0],True)


			apx1 = cv2.approxPolyDP(cnt1[0],eps1,True)
			apx2 = cv2.approxPolyDP(cnt2[0],eps2,True)


			cv2.drawContours(imgn,apx1,-1,255,1)
			cv2.drawContours(imgn1,apx2,-1,255,1)

			corn1 = cv2.goodFeaturesToTrack(imgn, 100, 0.01, 10)
			corn1 = np.int0(corn1)

			corn2 = cv2.goodFeaturesToTrack(imgn1, 100, 0.01, 10)
			corn2 = np.int0(corn2)

			no_corn1=len(corn1)
			no_corn2=len(corn2)

			if (no_corn1==no_corn2!=0 and A1==A2!=0 ):
				ok=1
				
			else :
				ok=0


			return ok

		else :
			ok=0
			return ok 
# 	* Function Name: <analyse_main(imag,imag1)>
# * Input: < imag,imag1>
# * Output: < value of the sum  >
# * Logic: <sum of values red green and blue filters and it calls function analyse>
	def analyse_main(imag,imag1):
		lowred=68
		upred=82
		lowblue=19
		upblue=36
		lowgreen=135
		upgreen=165


		filtred1=cv2.inRange(imag,lowred,upred)
		filtblue1=cv2.inRange(imag,lowblue,upblue)
		filtgrn1=cv2.inRange(imag,lowgreen,upgreen)

		filtred2=cv2.inRange(imag1,lowred,upred)
		filtblue2=cv2.inRange(imag1,lowblue,upblue)
		filtgrn2=cv2.inRange(imag1,lowgreen,upgreen)


		r=analyse(filtred1,filtred2)
		b=analyse(filtblue1,filtblue2)
		g=analyse(filtgrn1,filtgrn2)


		babu=r+b+g


		return babu
# * Function Name: <sliding_window>
# * Input: < image, stepSize, windowSize>
# * Output: < none >
# * Logic: <commpare value of two tiles one of which is stationary and the other is stationary >
	def sliding_window(image, stepSize, windowSize):
		# slide a window across the image
		for y in xrange(0, image.shape[0], stepSize):
			for x in xrange(0, image.shape[1], stepSize):
				# print x,y # yield the current window
				yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])
	#A* Search algorithm implementation to find the minimum path between 2 points
# * Function Name: <astar>
# * Input: < m,startp,endp>
# * Output: < a list with the planned shortest path >
# * Logic: <it takes the start point and  destination point and computes the path using the available graph(maze) >
	def astar(m,startp,endp):
	    w,h = 10,10		# 10x10(blocks) is the dimension of the input images
	    sx,sy = startp 	#Start Point
	    ex,ey = endp 	#End Point
	    #[parent node, x, y, g, f]
	    node = [None,sx,sy,0,abs(ex-sx)+abs(ey-sy)] 
	    closeList = [node]
	    createdList = {}
	    createdList[sy*w+sx] = node
	    k=0
	    while(closeList):
	        node = closeList.pop(0)
	        x = node[1]
	        y = node[2]
	        l = node[3]+1
	        
	        k+=1
	        #find neighbours 
	        if k!=0:
	            neighbours = ((x,y+1),(x,y-1),(x+1,y),(x-1,y))
	        else:
	            neighbours = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
	        for nx,ny in neighbours:
	            if nx==ex and ny==ey:
	                path = [(ex,ey)]
	                while node:
	                    path.append((node[1],node[2]))
	                    node = node[0]
	                return list(reversed(path))            
	            if 0<=nx<w and 0<=ny<h and m[ny][nx]==0:
	                if ny*w+nx not in createdList:
	                    nn = (node,nx,ny,l,l+abs(nx-ex)+abs(ny-ey))
	                    createdList[ny*w+nx] = nn
	                    #adding to closelist ,using binary heap
	                    nni = len(closeList)
	                    closeList.append(nn)
	                    while nni:
	                        i = (nni-1)>>1
	                        if closeList[i][4]>nn[4]:
	                            closeList[i],closeList[nni] = nn,closeList[i]
	                            nni = i
	                        else:
	                            break
	    return []



	# load the image and define the window width and height
	image = cv2.imread(image_filename)
	(winW, winH) = (60, 60)		# Size of individual cropped images 

	obstacles = []			# List to store obstacles (black tiles)  
	index = [1,1] #starting point
	#create blank image, initialized as a matrix of 0s the width and height
	blank_image = np.zeros((60,60,3), np.uint8)
	#create an array of 100 blank images
	list_images = [[blank_image for i in xrange(9)] for i in xrange(6)] 	#array of list of images 
	#empty #matrix to represent the grids of individual cropped images
	maze = [[0 for i in xrange(9)] for i in xrange(6)] 			

	#traversal for each square
	for (x, y, window) in sliding_window(image, stepSize=60, windowSize=(winW, winH)):
		# if the window does not meet our desired window size, ignore it
		if window.shape[0] != winH or window.shape[1] != winW:
			continue

	#	print index, image is our iterator, it's where were at returns image matrix
		clone = image.copy()
		#format square for openCV
		cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
		crop_img = image[x:x + winW, y:y + winH] 				#crop the image
		list_images[index[0]-1][index[1]-1] = crop_img.copy()			#Add it to the array of images

		#we want to print occupied grids, need to check if white or not
		average_color_per_row = np.average(crop_img, axis=0)
		average_color = np.average(average_color_per_row, axis=0)
		average_color = np.uint8(average_color)					#Average color of the grids

		#iterate through color matrix,
		if (any(i <= 240 for i in average_color)):				#Check if grids are colored
			maze[index[1]-1][index[0]-1] = 1				#ie not majorly white
			occupied_grids.append(tuple(index))				#These grids are termed as occupied_grids 

		if (any(i <= 20 for i in average_color)):				#Check if grids are black in color
	#		print ("black obstacles")
			maze[index[1]-1][index[0]-1] = 2
			obstacles.append(tuple(index))					#add to obstacles list

		#show this iteration


		#Iterate
		index[1] = index[1] + 1							
		if(index[1]>10):
			index[0] = index[0] + 1
			index[1] = 1


	#get object list
	list_colored_grids = [n for n in occupied_grids if n not in obstacles]	#Grids with objects (not black obstacles)


	#Compare each image in the list of objects with every other image in the same list
	#Most similar images return a ssim score of > 0.9
	#Find the min path from the startimage to this similar image u=by calling astar function

	for startimage in list_colored_grids:
		key_startimage = startimage
		#start image
		img1 = list_images[startimage[0]-1][startimage[1]-1]
		for grid in [n for n in list_colored_grids  if n != startimage]:
			#next image
			img = 	list_images[grid[0]-1][grid[1]-1]
			#convert to grayscale
			image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

			image2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


			#compare structural similarity

			s = analyse_main(image, image2)
			#if they are similar
			if s ==1:

			

				#perform a star search between both
				result = astar(maze,(startimage[0]-1,startimage[1]-1),(grid[0]-1,grid[1]-1))
	#			print result
				
				list2=[]
				for t in result:
					x,y = t[0],t[1]
					list2.append(tuple((x+1,y+1)))			#Contains min path + startimage + endimage
					result = list(list2[1:-1]) 			#Result contains the minimum path required 

				if not result:						#If no path is found;
					planned_path[startimage] = list(["NO PATH",[], 0])
				planned_path[startimage] = list([str(grid),result,len(result)+1])

	for obj in list_colored_grids:
		if not(planned_path.has_key(obj)):					#If no matched object is found;
			planned_path[obj] = list(["NO MATCH",[],0])			

	return occupied_grids, planned_path

# #### NO EDIT AFTER THIS

# DO NOT EDIT
# return Expected output, which is a list of tuples. See Task1_Description for detail.
occupied_grids, planned_path = main("test_images/test_image4.jpg")
print "Occupied Grids : "
print occupied_grids
print "Planned Path :"
print planned_path



'''
Below part of program will run when ever this file (task1_main.py) is run directly from terminal/Idle prompt.

'''
if __name__ == '__main__':

    # change filename to check for other images
    image_filename = "test_images/test_image4.jpg"

    main(image_filename)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
