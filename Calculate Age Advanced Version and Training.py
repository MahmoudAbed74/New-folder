age = int(input("enter your age: ").strip())

unit = input("enter your unit month/m or weeks/w or days/d : ").strip().lower()
month = age * 12
weeks = month * 4
days = weeks * 7 
hours = days * 24
if unit == "month" or unit == "m":
    month = age *12
    print(f"{month:,} month")
elif unit =="weeks" or unit == "w":
    weeks = month * 4
    print(f"{weeks:,} weeks")
elif unit =="days" or unit == "d":
    days = weeks * 30
    print(f"{days:,} days")
else :
    print("please enter the right value")        