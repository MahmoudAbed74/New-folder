# list1 =[1,2,3,4,5]
# list2 = ["A","B","C"]
#start less items  or anther mean it take count less items 
# ultimateList = zip(list1,list2)
# print(ultimateList)

# for item in ultimateList:
#     print(item)


list1 =[1,2,3,4,5]
list2 = ["A","B","C"]
tuple1 = ("man","wowen","girl","boy")
dict1 = {"mahmoud":"fname","mohammed":"mname","abed":"lastNmae"}
for item1,item2,item3,item4 in zip(list1,list2,tuple1,dict1):
    print("List1  is item >>=",item1)
    print("List2  is item >>=",item2)
    print("tuple1  is item >>=",item3)
    print("dictionary1  is item >>=",item4,"value",dict1[item4])