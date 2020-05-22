# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:14:18 2020

@author: eLtronicsvilla
"""
import time
import math
import numpy as np

def make_files():                                                                                      
    my_dict = {}
    for i in range(0,10):
          value = [ np.random.uniform(0,256) for j in range(256)]                                                                       
          my_dict["img"+"_"+str(i)] = value 
          
    np.save('my_dict.npy', my_dict)

def from_csv_via_np():  
    cal_sc = []
    a_f = [np.random.uniform(0,256)]
    iter_start = time.perf_counter()  
                                                                           
    arr = np.load('my_dict.npy',allow_pickle=True)
    for key,value in arr.item().items():
        b_f = value
        aa = sum([x*y for x,y in zip(a_f,a_f)])
        ab = sum([x*y for x,y in zip(a_f,b_f)])
        bb = sum([x*y for x,y in zip(b_f,b_f)])
        score = ab / math.sqrt(aa*bb)
        cal_sc.append((key,score))
    
    iter_elapsed = (time.perf_counter() - iter_start)
    print(f"    iter: {iter_elapsed} seconds")                                                                        
    return cal_sc


if __name__ == '__main__':                                                                           
    make_files()
    from_csv_via_np()
