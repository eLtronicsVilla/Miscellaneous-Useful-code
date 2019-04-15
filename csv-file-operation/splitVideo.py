#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 18:12:54 2019

@author: brijesh Gupta
"""

import cv2
import numpy as np
import os
import sys

if len(sys.argv)!=5:
	print('Invalid no of arguments')
	print('Usage : python splitVideo.py inputVideoname outputDirName skipFrames framesTobeSaved')
	print('Ex : python splitVide.py video_1.mp4 video_1 2 10')
	print('Note: Please store all input videos in videos directory')
	print('Note: All output images are stored in data directory with given outputDirName')
	sys.exit(1)

filename = sys.argv[1]
cap = cv2.VideoCapture(filename)
#cap = cv2.VideoCapture(0) #For webcam

outputDirName= str(sys.argv[2])

try:
	if not os.path.exists(outputDirName):
		os.makedirs(outputDirName)
except OSError:
	print('Error: creating directory of data')

currentFrame = 1
framesSaved = 0

while(True):
	ret,frame = cap.read() # Read frame
	if(ret==False):
		sys.exit(1)
	elif(currentFrame%int(sys.argv[3])==0):
		if (framesSaved>=int(sys.argv[4])):
		#if(False):
			print('No of frames saved-'+str(framesSaved)+' = '+'Required no of frames-'+str(sys.argv[4]))
			print('Exiting......!')
			sys.exit(1)
		else:
			outputFilename = outputDirName+'/frame-'+str(currentFrame)+'.jpg'
			print ('creating.....' + outputFilename)
			framesSaved +=1
			cv2.imwrite(outputFilename,frame)

	currentFrame+=1

cap.release()
cv2.destroyAllWindows()

