#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:57:22 2019

@author: brijesh Gupta
"""

# import the necessary packages
import cv2
import os, os.path
import sys
import csv
import time

if len(sys.argv)!=3:
	print('Invalid no of arguments')
	print('Usage : python specSheet.py input_dir_path Output_csv_file')
	print('Ex : python specSheet.py ./data/video_2 test.csv')
	sys.exit(1)

#debug info OpenCV version
print ("OpenCV version: " + cv2.__version__)
 
#image path and valid extensions
imageDir = sys.argv[1] #specify your path here
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]
 
#create a list all files in directory and
#append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))

#loop through image_path_list to open each image
with open(sys.argv[2],'a') as csvfile:
	filewriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['SN','Date','Object Name','Image Path','Opened-Eyes','Closed-Eyes'])
	todays_date = time.strftime("%Y-%m-%d %H:%M:%S")
	SN = 0
	for imagePath in image_path_list:
	    image = cv2.imread(imagePath)
	    img_resize = cv2.resize(image,(800,600))
	    
	    # display the image on screen with imshow()
	    # after checking that it loaded
	    if image is not None:
	        cv2.imshow(imagePath, img_resize)
	        key = cv2.waitKey(100)
	        #Opened_Eyes = raw_input("Enter the no of Opened-Eyes present: ")
	        Closed_Eyes = raw_input("Enter the no of Closed-Eyes present: ")
	        filewriter.writerow([str(SN),str(todays_date),'Eye',imagePath,0,Closed_Eyes])
	        SN+=1
	    elif image is None:
	        print ("Error loading: " + imagePath)
	        #end this loop iteration and move on to next image
	        continue

	    #key = cv2.waitKey(0)
	    if key == 27: # escape
	        break
	    cv2.destroyAllWindows()
csvfile.close()