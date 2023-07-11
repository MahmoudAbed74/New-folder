mylist=[1,2,"one","two",3,True]
print(mylist)
print(mylist[0])
print(mylist[1:4:2])
mylist[1:4]=["two"]
print(mylist)


print(myfriends)
mylist=[1,2,"one","two",3,True]
myfriends.append(mylist)
print(myfriends)
print(myfriends[4][3])

#exend()add list in list to is same the list
a=[1,2,3]
b=["a","b","c"]
c=["one","two","three"]
a.extend(b)
a.extend(c)
print(a)

#remove()
c=["one","two","three","one"]
c.remove("one")
print(c)

#sort
y=[1,5,3,4,7,9,12,22,2]
y.sort(reverse=True)#true=تنازلي
print(y)

#reverse

z = [10,2,5,478,5676,467,6464]
z.reverse
print(z)

z = [10,2,5,478,5676,467,6464]
z.clear()

#copy
z = [10,2,5,478,5676,467,6464]
a= z.copy()
print(z)
print(a)

#count
z = [10,2,2,2,2,5,478,5676,467,6464]
print(z.count(2))

#index 
z = [10,2,5,478,5676,467,6464]
print(z.index(5))

#insert
z = [10,2,5,478,5676,467,6464]
z.insert(0,"one")
print(z)

#pop
z = [10,2,5,478,5676,467,6464]
print(z.pop(2))
#clear
print(z.clear())

