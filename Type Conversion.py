#str()  convert type to string
a =10
print(type(a))
print(str(a))
print(type(str(a)))

#tuple()  convert type to tuple & not allow int
c = "osama"
d =[1,2,3]
e = {"s","e"}
f ={"a":1,"n":2}

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

#list()

#set()

#dict() convert type to tuple & not allow set & string
#c = "osama"
j =((1,"one",2,"two"))
i = [[1,"one"],[2,"two"]]
#k = {{2,"two"},{1,"one"}}
print(dict(i))
print(dict(j))
#print(dict(k))