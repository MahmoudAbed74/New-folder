import datetime 
# print(dir(datetime))
# print(dir(datetime.datetime))

#print current date and time 
print(datetime.datetime.now())

#print the current month
print(datetime.datetime.now().month)
#print the current day
print(datetime.datetime.now().day)

#print start and end of data
print(datetime.datetime.min)
print(datetime.datetime.max)

#print the time 
print(datetime.datetime.now().time())

print(datetime.datetime.now().time().hour)

#print specfific date
print(datetime.datetime(1982,10,25))


mydate =datetime.datetime(1982,10,25)
now = datetime.datetime.now()
my_age= now -mydate
print(my_age.days)
print(f"{my_age.days/365:.2n} year")

# Date And Time Format Date
mybirthday =datetime.datetime(1999,9,25)
print(mybirthday)
print(mybirthday.strftime("%a"))
print(mybirthday.strftime("%A"))
print(mybirthday.strftime("%b"))
print(mybirthday.strftime("%B"))
print(mybirthday.strftime("%d - %B - %Y"))