import numpy as np 

# my_list = [1,2,3,4]
# my_array = np.array(my_list)

# print(my_list)
# print(my_array)

# print("#"*50)
# #type
# print(type(my_array))
# print(type(my_list))

# print("#"*50)
# #element
# print(my_list[0])
# print(my_array[0])

# print("#"*50)

a=np.array(10)
b= np.array([10,20])
c= np.array([[10,20],[30,40]])
d = np.array([[[[[[[[[10,20,30],[50,60,70]]]]]]]]])

print(d[0,0,0,0,0,0,0,1,1])

print("#"*50)
#numbers of dimensions

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("#"*50)
#custom dimensions
my_custom_array= np.array([1,2,3,4],ndmin=3)
print(my_custom_array)