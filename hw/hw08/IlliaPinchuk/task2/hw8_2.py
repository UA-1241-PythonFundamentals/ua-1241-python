import re

def check_password_validity(password):
    if (6 <= len(password) <= 16 and
        re.search(r'[a-z]', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[$#@]', password)):
        return True
    return False

password = input("Enter your password: ")
print("Password is valid." if check_password_validity(password) else "Password is invalid.")
