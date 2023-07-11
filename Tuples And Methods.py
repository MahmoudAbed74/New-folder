mytuple=("ahmed","ali",3,4,True)
mytuple1="emad","saad"
print(mytuple)
print(mytuple1)
print(mytuple[0])

mytuple1="emad", #or mytuple1=("emad",)
print(type(mytuple1))
print(len(mytuple1))

a=(1,2,3,True)
b =(5,"ahmed")

c=a+b
d=a+("a",)
print(c)
print(d)
#tuple,list,string repeat(*)
myString="osama"
mylist=[1,2]
mytuple=("A","b")
print(myString*5)
print(mylist*5)
print(mytuple*5)
#count
a= (1,2,3,5,5,5,3)
print(a.count(5))
#index
h = (1,2,5,8,7,5)
print(f"the position of index is : {h.index(8)}")
# tuple destruct
a = ("a","b","c",5,True)
x,y,_,_#remove or not show item c and 5,z =a
print(x)
print(y)
print(z)