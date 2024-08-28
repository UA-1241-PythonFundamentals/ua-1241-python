import re

def password_validator(password):
    if len(p) not in range(6,16):
        return False
    elif not re.search(r"[a-z]", password):
        return False
    elif not re.search(r"[A-Z]", password):
        return False
    elif not re.search(r"[0-9]", password):
        return False
    elif not re.search(r"[@#\$]", password):
        return False
    else:
        return True

p = input("Provide password for validation: ")

if password_validator(p):
    print(f"Password {p}, is valid")
else:
    print(f"Password {p} is not valid")