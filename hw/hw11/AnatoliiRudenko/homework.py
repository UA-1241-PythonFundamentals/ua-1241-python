def age(age):
    try:
        if age<0:
            raise ValueError("Wrong value")
        age=input("Enter age: ")
        if age%2==0:
            print("Age is even")
        elif age%2==1:
            print("Age is odd")
    except ValueError:
        print(ValueError)

def weekday():
    day=int(input("Enter day of week: "))
    try:
        if day==1:
            print("Monday")
        elif day==2:
            print("Tuesday")
        elif day==3:
            print("Wednesday")
        elif day==4:
            print("Thursday")
        elif day==5:
            print("Friday")
        elif day==6:
            print("Saturday")
        elif day==7:
            print("Sunday")
        elif day>=8 or not isinstance(day, int):
            raise ValueError
    except ValueError:
        print("Wrong value")
