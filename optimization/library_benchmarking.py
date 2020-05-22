
import time  
import math                                                                                        
import numpy as np 
import pandas as pd                                                                                   
import dask.array as da          #dask with numpy                                                                    
import dask.dataframe as dd      #dask with pandas
                                                                        
def simple_files():                                                                                    
    #a = np.random.random(256)                                                                              
    mat = np.random.uniform((100000, 256))                                                                
    np.savetxt('data.csv', mat, delimiter=',', header=','.join(str(x) for x in range(256))) 
    
def make_files():                                                                                    
    #a = np.random.uniform(256)   
    my_dict = {}
   # value = []
    for i in range(0,100000):
          value = [ np.random.uniform(0,1) for j in range(256)]                                                                       
          my_dict["img"+"_"+str(i)] = value 
    
   # print(my_dict)                                 
   # with open('data.csv', 'w') as f:
       # for key, value in my_dict.items():
        #    f.write('%s%s\n' % (key, value))
    np.save('my_dict.npy', my_dict)

def from_csv_via_np():  
    cal_sc = []
    iter_start = time.perf_counter()                                                                             
    #arr = np.loadtxt('data.csv', delimiter=',', skiprows=1)
    a_f = [np.random.uniform(0,256)]
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

          

def from_csv_via_nnp():                                                                               
    arr = np.loadtxt('data.csv', delimiter=',', skiprows=1)
   # for key,value in arr.items:
                                                                            
    return arr

def from_csv_via_da():                                                                               
    mat = np.loadtxt('data.csv', delimiter=',', skiprows=1)                                          
    arr = da.from_array(mat,chunks="auto")                                                                         
    return arr
          

def from_csv_via_df():                                                                               
    df = dd.read_csv('data.csv')                                                                     
    arr = df.to_dask_array(lengths=True)                                                              
    return arr                                                                                       

def benchmark(fn):                                                                                   
    arr = fn()                                                                                       

    iter_start = time.perf_counter()                                                                 
    n_iters = 1                                                                                     
    for i in range(n_iters):
        if fn is from_csv_via_da or fn is from_csv_via_df:                                                                         
            x = arr[i].compute()
        else:
            x = arr[i]                                                                         

    iter_elapsed = (time.perf_counter() - iter_start)/n_iters                                        

    print(f"func: {fn.__name__}")                                                                    
    #print(f"    array: {repr(arr)}")                                                                 
   # print(f"    read: {read_elapsed} seconds")                                                       
    print(f"    iter: {iter_elapsed} seconds")                                                       
    print(f"    size: {arr.nbytes} bytes")                                                           

if __name__ == "__main__":                                                                           
    make_files()   
    from_csv_via_np()                                                                                  
    #benchmark(from_csv_via_np)
    #benchmark(from_csv_via_da)                                                                       
    #benchmark(from_csv_via_df)                                                                       
