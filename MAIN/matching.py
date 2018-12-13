import cv2
import numpy as np


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

def divide_and_match(main_image):


	w,h = main_image.shape

	door_area = main_image[0:h , 0:w/9]

	workspace = main_image[0:h , w/9:w]



	matched = []
	list_of_door_cell_image = []
	w_door,h_door = door_area.shape
	w_workspace,h_workspace = workspace.shape

	cell_width_door = w_door
	cell_height_door = h_door/6

	cell_width_workspace = w_workspace/8
	cell_height_workspace = h_workspace/6

	for j in range(6):
		for i in range(9):
			if i == 0 :
				i_door_img = door_area[j*cell_height_door : j*cell_height_door + cell_height_door , i*cell_width_door : i*cell_width_door + cell_width_door]
				list_of_door_cell_image.append(i_door_img)

	for a in range(6):
		for j in range(6):
			for i in range(9):
				if i != 0 :

					i_workspace_img = door_area[j*cell_height_workspace : j*cell_height_workspace + cell_height_workspace , i*cell_width_workspace : i*cell_width_workspace + cell_width_workspace]
					s = analyse_main(list_of_door_cell_image[a],i_workspace_img)

					if s == 1 :
						matched.append(((0,a),(i,j)))

					else :
						match = False


	return matched