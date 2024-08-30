import re
def check_password(password):
    if len(password) < 6 or len(password) > 16:
        return False

    if not re.search("[a-z]", password):
        return False

    if not re.search("[A-Z]", password):
        return False

    if not re.search("[0-9]", password):
        return False

    if not re.search("[!@#$%^&*()_+]", password):
        return False

    return True

password = input("Enter your password:")

if check_password(password):
    print("Password is correct.")
else:
    print("Password isn't correct.")
