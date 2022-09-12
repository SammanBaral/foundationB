age=int(input("please provide your age:"))
#conditional statement
#if block only
print("Code started . . . .")
if age>18:
    print(f"You can play this game because you are {age}")
    print("Code ended . . . .")
    #if-else block
    if age>18:
        print(f"You can play this game because you are {age}")
    else:
            print("You need to be above 18 years old")
##proper use of if-elif-else block
if age<0:
    print("Please input your valid age")
elif 0<=age<=10:
    print("So you are kid,your movie ticket is 100")      
elif 10<age<20:
    print("Your movie ticket is 200")
else:
    print("Your movie ticket is 300")      
