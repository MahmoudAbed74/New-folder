# Do it find in varabile ?

print("n" in "name")#true
print("h" in "name")#false
print("A" in "name")#false

my_friends = ["mahmoud","ahmed","ali"]
print("mahmoud" in my_friends)#true
print("ahmed"not in my_friends )#false

my_country =["egypt","ksa","iraq"]
country = input("please enter your country: ")

if country in my_country:
    print("yeah, it is fantastic")
else:
    print("try again")    

# Practical Membership Control        

admins = ["ahmed","ali","saad","alaa"]
name = input("enter the name")

if name in admins:
    print(f"hello {name} in admins")
    new_value = input("enter your update or delete the name")
    if new_value == "update" or "u":
        new_name = input("enter the new name: ").strip().capitalize()
        admins[admins.index(name)]=new_name
        print(new_name)
        print(admins)
    elif new_value =="delete" or new_value == d:
        admins.remove(name)
        print("delete the name")
        print(admins)    
elif name not in admins:
    print("the name not damin")
    stautas = input("add to the admins ")        
    if stautas == "yes":
        admins.append(name)
        print(admins)
    else :
        print("you nit admin")    

