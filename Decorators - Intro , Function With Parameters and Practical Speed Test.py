def myDecorator1(func): #Decorator
    def nestedfunc(): #Any Name Its just for Decoration
        print("before")# message from decorator

        func() #execute function

        print("After")#message from decorator

    return nestedfunc #Return All data           
@myDecorator1
def sayHello():

    print("Hello from Say Hello Function")
@myDecorator1
def helloAreYou():
    print("hello ,how are you?")
## Instad of ##

# afterDecoration = myDecorator(sayHello)
# afterDecoration()

sayHello()
print("#"*50)
helloAreYou()

# Function With Parameters

# def myDecorator1(func): #Decorator
#     def nestedfunc(num1,num2): #Any Name Its just for Decoration
#         print("before")# message from decorator

#         func(num1,num2) #execute function

#         print("After")#message from decorator

#     return nestedfunc #Return All data           

# @myDecorator1
# def caculator(num1,num2):
#     print(num1 + num2)
# caculator(10,50)    

def mydecorator2(func):
    def nestedfunction(num1,num2):
        if num1 > 10 and num2 > 15 :
            print("the numbers is True")
        else:
            print("the numbers is false")
        func(num1,num2)

    return nestedfunction 

def mydecorator3(func):
    def nestedfunction(num1,num2):
        if num1 > 10 and num2 > 15 :
            print("the decorator 3 ")
        else:
            print("the decorator 3")
        func(num1,num2)

    return nestedfunction 
@mydecorator3    
@mydecorator2
def caculator1(n1,n2):
    print(n1 + n2)

@mydecorator2
@mydecorator3
def caculator2(num1,num2):
    print(num1 - num2)                    

caculator1(15,20)
caculator1(2,25)

print("#"*50)
caculator2(25,20)
caculator2(30,2)

# #decorator 
# def mydecorator(fun):
#     def nestedfunction(*number):
#         for n in number:
#             if n > 0:
#                 print("the number is true")
#         fun(*number)
#     return nestedfunction

# @mydecorator
# def calcultor(n1,n2,n3,n4):
#     print(n1+n2+n3+n4)    

# calcultor(15,2,0,3)

from time import time

def speedTest(func):
    def Run_time():
        start = time()
        func()
        end = time()

        print(f"the run time is {end-start:.2f}")
    return Run_time
@speedTest
def bigrun():
   for n in range(1,20000):
       print(n)
bigrun()       