# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:14:54 2020

@author: eLtronicsvilla
"""

import time
import math
import numpy as np
import concurrent.futures
from threading import Thread 

def make_files():                                                                                      
    my_dict = {}
    for i in range(0,100000):
          value = [ np.random.uniform(0,256) for j in range(256)]                                                                       
          my_dict["img"+"_"+str(i)] = value    
    np.save('my_dict.npy', my_dict)

def from_csv_via_np():  
    cal_sc = []
    iter_start = time.time()                                                                             

    a_f = [np.random.uniform(0,256)]
    arr = np.load('my_dict.npy',allow_pickle=True)
    for key,value in arr.item().items():
        b_f = value
        
       # aa=map(lambda x,y:x*y,a_f,a_f)
       # ab=map(lambda x,y:x*y,a_f,b_f)
       # bb=map(lambda x,y:x*y,b_f,b_f)
       #aa,ab,bb = map(lambda x,y:x*y,a_f,a_f),map(lambda x,y:x*y,a_f,b_f),map(lambda x,y:x*y,b_f,b_f)
       # aa,ab,bb = list(map(sum,[map(lambda x,y:(x*y),a_f,a_f)])),list(map(sum,[map(lambda x,y:(x*y),a_f,b_f)])),list(map(sum,[map(lambda x,y:(x*y),b_f,b_f)]))
        
        aa = sum([x*y for x,y in zip(a_f,a_f)])
        ab = sum([x*y for x,y in zip(a_f,b_f)])
        bb = sum([x*y for x,y in zip(b_f,b_f)])
        #aa,ab,bb = sum([x*y for x,y in zip(a_f,a_f)]),sum([x*y for x,y in zip(a_f,b_f)]),sum([x*y for x,y in zip(b_f,b_f)])
        score = ab / math.sqrt(aa*bb)
        cal_sc.append((key,score))
    
    iter_elapsed = (time.time() - iter_start)
    print(f"    iter: {iter_elapsed} seconds")                                                                        
    return cal_sc

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(from_csv_via_np)
        return_value = future.result()
    #print(future.done())
    #time.sleep(2)
    #print(future.done())
    #print(return_value)


if __name__ == '__main__':                                                                           
    make_files()
    #main()
    from_csv_via_np()
    #t1 = Thread(target=from_csv_via_np)
    #t1.start()
    #t1.join()
