"""
These program helps you know if your car can circulate in CDMX or not  and when is your verification month depending on the plate termination

Pseudocode:
1. Ask for the plate termination
2. Check if it is posible to circulate 
3. Show if it is possible circulate or not and which are your verification months

"""


choice=int(input(f"""This program helps you know if your car can circulate in CDMX or not  and when is your verification month depending on the plate termination
Type:
1. Month of validation
2. Circulation day
3. Exit  
"""))

if choice==1:
    termination=int(input("Type termination of your plate: "))
    if termination<0 or termination>9:
        print("It does not exists")
    elif termination==1 or termination==2:
        print(f"Your validation months are January and February")
    elif termination==3 or termination==4:
        print(f"Your validation months are March and April")
    elif termination==5 or termination==6:
        print(f"Your validation months are May and June")
    elif termination==7 or termination==8:
        print(f"Your validation months are June, August")
    elif termination==0 or termination==9:
        print(f"Your validation months are November")
    exit()
elif choice==2:
    termination=int(input("Type termination of your plate: "))
    if termination<0 or termination>9:
        print("It does not exists")
    elif termination==1 or termination==2:
        print(f"You can circulate on Thursday")  
    elif termination==3 or termination==4:
        print(f"You can circulate on Wednesday")
    elif termination==5 or termination==6:
        print(f"You can circulate on Monday")
    elif termination==7 or termination==8:
        print(f"You can circulate on Tuesday")
    elif termination==0 or termination==9:
        print(f"You can circulate on Friday")
elif choice==3:
    print("You have exited the program")
    exit()
else:
    print("Invalid option")