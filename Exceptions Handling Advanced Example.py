the_file = None
Tries=5

while Tries > 0 :
    try:
        print("enter the file Name with Absoute path to open")
        the_file_and_path = input("enter the path:- ").strip()
        the_file = open(the_file_and_path,'r')
        print(the_file.read())

        break
    except FileNotFoundError:
        print("the file not found")
        Tries -= 1
        print(f"tries is {Tries} left")
    except :
        print("error happenies")
        Tries -= 1
    finally :
        if the_file is not None:
            the_file.close()
            print("the file is closed")        
else:
    print("the tries is done")            