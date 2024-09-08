"""Task 1"""

def user_age(age):
    if int(age) < 0:
        raise ValueError("You have entered a negative age. This is not possible :)")
    elif int(age) % 2 == 0:
        print("Your age is an even number.")
    elif int(age) % 2 != 0:
        print("Your age is an odd number.")


try:
    age = input("Please, enter your age: ")
    user_age(age)
except ValueError as error:
    print("Mistake: ", error)


"""Task 2"""
def get_day(day_number):
    if int(day_number) <= 0 or int(day_number) > 7:
        raise ValueError("You have entered wrong number of day in a week.")
    elif not int(day_number):
        raise TypeError("Please, enter the exact number: ")
    else:
        week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Weekend"}
        print(f"The day with number {day_number} in a week is a {week.get(int(day_number))}")
    pass

run = True

while run:
    try:
        day_number = input("Please, enter the number of the day of the week: ")
        get_day(day_number)
    except ValueError as error:
        print("Mistake: ", error)
    except TypeError as error:
        print("Mistake: ", error)
