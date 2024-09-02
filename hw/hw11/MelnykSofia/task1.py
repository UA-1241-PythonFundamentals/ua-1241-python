
def user_age():
    try:
        age = int(input("Enter user age: "))
        if age <= 0:
            raise ValueError("That is not age! That is not a positive number.")

        if age%2==0:
            print (f"Your age {age} is even")
        elif not age%2==0:
            print (f"Your age {age} is odd")
    except ValueError:
        print(ValueError)


user_age()