def check_age(age):
    if age <= 0:
        raise ValueError("Incorrect age")

def get_age_from_user():
    while True:
        try:
            age = int(input("Please enter your age: "))
            check_age(age)
            return age
        except (ValueError, TypeError):
            print("Invalid input. Please enter a natural number.")

user_age = get_age_from_user()
print(f"Your age is: {user_age}")