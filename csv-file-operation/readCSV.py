#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:03:14 2019

@author: brijesh Gupta
"""

import csv
import numpy as np

with open('test.csv', 'rb') as f:
	reader = csv.DictReader(f)
	no=1
	for row in reader:
		#path = row
		print row['Image Path'],row['Closed-Eyes'],row['Opened-Eyes']
		#print path

		