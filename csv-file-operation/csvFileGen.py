#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:03:34 2019

@author: brijesh Gupta
"""


'''import csv

with open('Test.csv','wb') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['objectName','Path','imageName','No of Objects','Comments'])

csvfile.close()'''
'''------------------------------------------------------------------------'''
'''import csv

with open('Test.csv','wb') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['objectName','Path','imageName','No of Objects','Comments'])
	input = input("Enter the no of objects present in a file:")
	filewriter.writerow(input)

csvfile.close()'''
'''-------------------------------------------------------------------------'''

'''import csv
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

csvfile.close()'''
''' ---------------------------------------------------------------------------------------'''
'''import sys
import time

if len(sys.argv) != 2:
    print "usage: {} <output_file_name>".format(sys.argv[0])
    sys.exit(1)

filename = sys.argv[1]
with open(filename, 'wb') as target_file:

	target_file.write('objectName','Path','imageName','No of Objects','Comments')
    workout = raw_input("Enter what workout you did today: ")
    num_sets = raw_input("Enter the number of sets you did today")
    num_reps = raw_input("Enter the number of reps per set you did today")
    weight = raw_input("Enter the weight you lifted today")

    # you might also want to record the day and time you worked out [4]
    todays_date = time.strftime("%Y-%m-%d %H:%M:%S")

    # this says "join each element in the passed-in tuple/list 
    # as a string separated by a comma"
    workout_entry = ','.join((workout, num_sets, num_reps, weight, todays_date))

    # you don't need to save all the entries to a list, 
    # you can simply write the workout out to the file obj `target_file`
    target_file.write(workout_entry)

    # Note: I removed the `target_file.close()` because the file closes when the 
    # program reaches the end of the `with` statement.'''