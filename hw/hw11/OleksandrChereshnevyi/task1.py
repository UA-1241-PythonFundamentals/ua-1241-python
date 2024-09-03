def age_helper():
    try:
        age =  int(input("Enter your age: "))
        if age <= 0 or age > 130:
            raise ValueError("That is not a positive number!")
        if (age % 2 == 0):
            print("Even")
        else:
            print("Odd")

    except ValueError as e:
        print(e)
    except:
        print("Something went wrong")

age_helper()