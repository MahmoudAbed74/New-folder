my1_string ='''first
second
third'''
my_string= """first
second 'test' \ "test"
third"""
print(my_string)
print(my1_string)

#indexing (Access Single item)
my_string1 = "i love python"
print(my_string1[0])
print(my_string1[8])

print(my_string1[-1])

#Slicing (Access multi item)
#[start:End]end not inculded
#[Start:End:Steps]
my_string = "i love python"

print(my_string[8:11])
print(my_string[:11])
print(my_string[0::2])
print(my_string[3:11:3])

my_string = "i love python"
#strip() , rstrip() ,lsrip() remove the space deafolt

a = "     I love python        "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#########I love ####python##########"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

# title
b = "I love python 3b"
print(b.title())

c = "I love python 3b"
print(c.capitalize())

#zfill
a,b,c ="1" ,"11","111"
print(a)
print(b)
print(c)

print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))

#upper
c = "I love python 3b"
print(c.upper())

#lower
print(c.lower())


#split, rsplit
c = "I love python 3b"
d = "I-love-python-3b"
print(c.split())
print(d.split("-",2))#number of items in list

print(c.rsplit())
print(d.rsplit("-",2))#number of items in list

#center
a="mahmoud"
print(a.center(9))
print(a.center(9,"#"))

#count()

f= "i love python and php because php is easy "
print(f.count("php"))
print(f.count("php",0,25))#start : end to search

#swapcase
g ="i love python"
h ="i LOve pYThon"

print(g.swapcase())
print(h.swapcase())

#startswith()
m ="i love python"
print(m.startswith("i"or "I"))
print(m.startswith("p"))
print(m.startswith("o",3,12))

#endswith
j ="i love python"
print(j.endswith("n"or "I")) 
print(j.endswith("p"))
print(j.endswith("o",3,12))

#find
#index #want to search 

b= "i love python"
print(b.find("p"))#index number 
print(b.find("p",0,10))
print(b.find("p",0,5))

#rjust(width,fill char) #ljust(width,fill char) 
c ="mahmoud"
print(c.rjust(10))
print(c.rjust(10,"#"))

c ="mahmoud"
print(c.ljust(10))
print(c.ljust(10,"#"))

#splitlines()
e ="""first line
second line
third line"""
print(e.splitlines())

# expandtaps()

g="hello\tworld\ti\tlove\tpython"
print(g.expandtabs(1))

one = "i love python and 3g"
print(one.istitle())


my_string = "i love python"
#strip() , rstrip() ,lsrip() remove the space deafolt

a = "     I love python        "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#########I love ####python##########"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

# title
b = "I love python 3b"
print(b.title())

c = "I love python 3b"
print(c.capitalize())

#zfill
a,b,c ="1" ,"11","111"
print(a)
print(b)
print(c)

print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))

#upper
c = "I love python 3b"
print(c.upper())

#lower
print(c.lower())

#replace(old value,new value,count)

a="Hello one one one two three "