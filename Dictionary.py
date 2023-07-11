#dictionary
#key:value
#key not allowed list

user={
    "name":"mahmoud",
    "age":15,
    "country":"egypt",
    (1,2,3,4):"true",
    1:"one",
    "skils":["css","python"]
}
print(user)
print(user["age"])
print(user.get("age"))

print(user.keys())#print all keys
print(user.values())#print all values

print("#"*50)
#two_dimnsional dictionary

languages = {
    "one":{
        "name":"html",
        "progress":"80%",
    },
    "Two":{
      "name":"html",
        "progress":"80%",  
    },
    "three":{
        "name":"css",
        "progress":"80%",
    }
}
print(languages)
print(languages["three"]["name"])
print(len(languages))
print(len(languages["three"]))
print(len(languages["three"]["name"]))

print("#"*50)

languages2={
    "one":{
        "name":"html",
        "progress":"80%"
    }
}
languages3={
    "one":{
        "name":"html",
        "progress":"80%"
    }
}
languages4={
    "one":{
        "name":"html",
        "progress":"80%"
    } 
}   
alllanguages={
    1:languages2,
    2:languages3,
    3:languages4
}    
print(alllanguages)

#clear
user ={
    "name":"mahmoud"
}
print(user)
user.clear()
print(user)

print("#"*50)
member = {
    "name":"ali"
}
member["age"]=50
print(member)
#or update
member.update({"rate":"5.3"})
print(member)
print("#"*50)

#copy
a ={
    "name":"ahmed"
}
b=a.copy()
print(b)

#setdefault
user ={
    "name":"mahmoud"
}
print(user)
print(user.setdefault("name","ahmed"))
print(user)
print(user.setdefault("age",36))
print(user)
print(user.setdefault("tamer"))
print(user)

print("#"*60)
#popitem 
member ={
    "name":"mahmoud"
}
member.update({"age":36})
print(member.popitem())

print("#"*60)
#items 

view={
    "name":"osama",
    "skill":"xbox"
}
allitems = view.items()
print(allitems)
view["age"]=14
print(allitems)
print(type(allitems))

#fromkeys
a=(1,2,3)#keys
b ="one","two" #values
print(dict.fromkeys(a,b))