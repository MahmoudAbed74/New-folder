#Generators 
#[1] Geneator is a functionwith "yield"keyword Instad of "return"
#[2] it support iteration  and Return Generator Iterator By Calling "yield"
#[3] Generator function can have one or more "yield"
#[4] by using next() It Resum for where it called "yield" not from begining 
#[5] when called , its not start Automatically,Its Only Give you the control 

def myGenerate():

    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
print(type(myGenerate()))    

Gen = myGenerate()
print(next(Gen))
print("Hello","mahmoud",sep=" ")
print(next(Gen))
print("Hello","from","Python",sep="&")
print(next(Gen))
print("Hello","from","Python",sep="&")
print(next(Gen))

for num in Gen:
    print(num)

