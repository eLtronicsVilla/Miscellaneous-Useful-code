#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:23:34 2019

@author: brijesh Gupta
"""

# import the necessary packages
import cv2
import sys
import os, os.path
 
#debug info OpenCV version
print ("OpenCV version: " + cv2.__version__)
 
#image path and valid extensions
imageDir = sys.argv[1] #specify your path here
outputDir= './data/val_image/'
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]
 
#create a list all files in directory and
#append files with a vaild extention to image_path_list
for i in range(14):
	dirName=imageDir+str(i)
	for file in os.listdir(dirName):
	    extension = os.path.splitext(file)[1]
	    if extension.lower() not in valid_image_extensions:
	        continue
	    image_path_list.append(os.path.join(dirName, file))

print(image_path_list)
print(len(image_path_list))

#sys.exit(1)
currentFrame = 1
#loop through image_path_list to open each image
for imagePath in image_path_list:
    image = cv2.imread(imagePath)
    # display the image on screen with imshow()
    # after checking that it loaded
    if image is not None:
        #cv2.imshow(imagePath, image)
        #key = cv2.waitKey(0)
        #if key == 115:
        outputFilename = outputDir+'/image'+str(currentFrame)+'.jpg'
        cv2.imwrite(outputFilename,image)
        print('writing image to'+str(outputFilename))
        currentFrame += 1
        cv2.destroyAllWindows()
        #elif key == 27:
        #	break
    elif image is None:
        print ("Error loading: " + imagePath)
        #end this loop iteration and move on to next image
        continue

    key = cv2.waitKey(1000)
    if key == 27: # escape
        break

    cv2.destroyAllWindows() 