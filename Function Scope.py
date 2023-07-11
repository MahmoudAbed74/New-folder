x = 1   #global scope

def one():
    global x
    x = 2   #function scope
    print(f"the function scope is {x}")
    

 
def two():
    x = 4   #function scope
    print(f"the function scope is {x}")
print(f"the global scope is   {x}")
one()
two()
print(f"the global scope is   {x}")
