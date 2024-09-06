def age_checker():
    try:
        age = int(input("Please, enter your age: "))

        if age < 0:
            raise ValueError("Age can not be negative")

        if age % 2 == 0:
            print("Your age is eval")
        else:
            print("Your age is odd")
    except ValueError as e:
        print(f"Error: {e}")


# age_checker()

def week_day():
    try:
        day_number = int(input("Please, enter number of day: "))

        if day_number not in range(1, 7):
            raise ValueError("This is not valid number of the day")

        match day_number:
            case 1:
                print('Monday')
            case 2:
                print('Tuesday')
            case 3:
                print('Wednesday')
            case 4:
                print('Thursday')
            case 5:
                print('Friday')
            case 6:
                print('Saturday')
            case 7:
                print('Sunday')
    except ValueError as e:
        print(f"Error: {e}")


week_day()
