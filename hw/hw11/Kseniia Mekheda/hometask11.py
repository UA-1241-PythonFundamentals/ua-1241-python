# Task 1
def check_age(age):
    if age < 0:
        raise ValueError("Your age can`t be negative") 
    elif age % 2 == 0:
        print("Your age is even")
    elif age % 2 != 0:
        print("Your age is odd")


try:
    age = int(input("Enter your age: "))
    check_age(age)
except ValueError as e:
    print("Oops, error:", e)

# Task 2
def name_day_by_number(day):
    days_dict = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    if day in days_dict:
        print(f"{day} day in a week is {days_dict[day]}")
    elif day > 7 or day < 1:
        raise KeyError("Invalid number - there are only 7 days in a week")
    
try:
    day = int(input("Enter the day of the week like a number: "))
    name_day_by_number(day)
except ValueError as e:
    print("Value Error:", e)
except KeyError as e:
    print("Error:", e)
