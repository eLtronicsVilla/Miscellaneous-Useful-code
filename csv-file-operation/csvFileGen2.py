#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:23:34 2019

@author: brijesh Gupta
"""

import csv
import os
import sys
import time

with open('Test.csv','wb') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['SN','Date','objectName','Path','imageName','No of Objects','Comments'])
	todays_date = time.strftime("%Y-%m-%d %H:%M:%S")
	SN = 0
	no_of_objects = input("Enter the no of objects present in a file: ")
	comments = input("Enter the comments on the current image: ")
	filewriter.writerow([str(SN),str(todays_date),'Eye',str(os.getcwd()),str(sys.argv[0]),no_of_objects,comments])

csvfile.close()