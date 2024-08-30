def get_week(number):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if 1 <= number <= 7:
        return days[number - 1]
    else:
        raise ValueError("Error.Number must be between 1 and 7.")

try:
    number = int(input("Enter a number: "))
    day = get_week(number)
    print(f" Day of the week is: {day}")
except ValueError as e:
    print(e)
except TypeError:
    print(" Enter a valid number.")
