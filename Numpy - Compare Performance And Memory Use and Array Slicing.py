import numpy as np 
import time 
import sys

element = 189000 
my_list= range(element)
my_list2=range(element)
# for r in my_list:
#     print(r)

# # for r in my_array:
# #     print(r)    
# list_start= time.time()   
# list_result=[(n1+n2) for n1,n2 in zip(my_list,my_list2)]
# # for n1,n2 in zip(my_list,my_list2):
# #     print(n1+n2)
# list_end=time.time()
# list_execute=list_end-list_start
print("#"*50)
my_array=np.arange(element)
my_array2=np.arange(element)

array_start= time.time()   
array_result=my_array+my_array2
# for n1,n2 in zip(my_array,my_ array2) :
#     print(n1+n2)
array_end=time.time()
array_execute=array_end-array_start
print(array_execute) 
# print(list_execute)    

# Array Slicing
myarray = np.array([[1,2,3],[7,8,9]])
print(myarray[0:1,:2])