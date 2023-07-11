myset={"osmaa","ahmed",100,True,100}#remove repeat
print(myset)
#print random items
myset1={"osmaa","ahmed",100,True,[1,2,3]}#unhashable type: 'list'
myset2={"osmaa","ahmed",100,True,(1,2,3)}

#clear
set2={"osmaa","ahmed",100,True,(1,2,3)}
print(set2.clear())

#union()
b={1,2,3}
c={"a","b","c"}
d={1}
print(b | c)
print(b.union(c,d))
#add
f= {1,2,3,4}
f.add(6)
f.add(7)
#dont add two item about add(5,6)

#copy
e={1,2,3}
r=e.copy()

print(e)
print(r)

e.add(6)

print(e)
print(r)

#remove
g={1,2,3}
g.remove(1)
print(g)
#print(g.remove(7))#KeyError: 7

#discard
h={1,2,3}
h.discard(1)
print(h)
print(h.discard(7))
print(h)
#pop()

i={1,2,3,4,5,6}
print(i.pop())

# update
k={1,2,3}
l={"a","b","c"}
m={1,"l"}
u=["css","html"]
k.update(l,m,u)
print(k)

#difference
b={1,2,3}
c={3,"a","b","c"}
print(b)
print(b.difference(c))
print(b-c)
print(b)
print("---"*60)
#difference_update 
l={1,2,3}
m={3,"a","b","c"}
print(l)
l.difference_update(m)
print(l)
print(l-m)
print(l)

#intersection() التقاطع

e={1,2,3,4,"x"}
f={1,2,"t","g"}

print(e)
print(e.intersection(f))#e&f
print(e)

print("#"*60)
#intersection_update()

g={1,2,3,4,"x"}
r={1,2,"t","g"}

print(g)
g.intersection_update(r)
print(g)
print("#"*60)

#symmetric_difference() &!
v={1,2,3,4,"x"}
p={1,2,"t","g"}

print(v.symmetric_difference(p))
print(v)

print("#"*60)
#symmetric_difference_update()
o={1,2,3,4,"x"}
z={1,2,"t","g"}
o.symmetric_difference_update(z)
print(o)

#issuperset()

a={1,2,3,4} #original set
b={1,2,3}
c={1,2,3,4,5}

print(a.issuperset(b))# Do b items in a items? true or flase (true)
print(a.issuperset(c)) #Do c items in a items? true or flase (flase)
print("#"*50)
#issubset 
d={1,2,3,4} #original set
e={1,2,3}
f={1,2,3,4,5}

print(d.issubset(e))# Do d items in e items? true or flase (flase)
print(e.issubset(d))# Do e items in d items? true or flase (true)

print("#"*50)

#isdisjoint 
g={1,2,3,4} #original set
h={1,2,3}
k={11,12,13}

print(g.isdisjoint(h))#flase
print(h.isdisjoint(k))#true
