def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."

try:
    age = int(input("Enter your age: "))
    message = check_age(age)
    print(message)
except ValueError as e:
    print(e)
