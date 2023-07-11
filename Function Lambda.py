def say_hello(name,age):
   return f"hello {name} and your age is : {age} "
print(say_hello("mahmoud", 36))   

# Function Lambda
hello = lambda name,age :f"hello {name} and your age is : {age}"# lambda :  in same line
print(hello("osama",24))

print(say_hello.__name__)
print(hello.__name__)