#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 10:47:15 2019

@author: brijesh Gupta
"""

# import the required library
import cv2
import sys
#capture the video from IP camera
#cap = cv2.VideoCapture("rtsp://username:password@ipadress:port")
# capture the video from USB camera
cap  = cv2.VideoCapture(0)
# get the width and height of the frame
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# video code to save the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(sys.argv[1], fourcc, 15.0, (int(width),int(height)))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,180)
        out.write(frame)
        cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()

out.release()

cv2.destroyAllWindows()
