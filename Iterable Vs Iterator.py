#iterable
# [1] object countains data that can be interated upon
# [2] examples (string , list , set , tuple, dictionary)

mystring ="osama"

myList =[1,2,3,4,5]

# for letter in mystring:
#     print(letter, end=" ")

# for number in myList:
#     print(number, end=" ")

## number = 15 # not interable
## for part in mynumber:
##     print(part , end= " ")    

#iterator 

myIterator1 = iter(mystring)

print(next(myIterator1))
print(next(myIterator1))

num = 15
string =str(num)
for n in string:
    print(n)
print(next(iter(string)))
