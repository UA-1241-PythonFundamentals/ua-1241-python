age = int(input("Enter your age",))
def print_age(age):
    try:
        if age%2 == 0 and age>0:
            print("chet")
        elif age%2 != 0 and age>0:
            print("nechet")
        else:
            raise Exception
    except: 
        print("Age can not be negative!") 

print_age(age)
