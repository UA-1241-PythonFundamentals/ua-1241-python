import re

def pas_validator(password):
    if (len(password) < 6 or len(password) > 16):
        return False
    elif len(re.findall("[a-z]", password)) == 0:
        return False
    elif len(re.findall("[A-Z]", password)) == 0:
        return False
    elif len(re.findall("[\\d]", password)) == 0:
        return False
    elif len(re.findall(r'#', password)) == 0 and len(re.findall(r'$', password)) == 0 and len(re.findall(r'@', password)) == 0:
        return False
    return True

while True:
    password = input("Please input password: ")
    if pas_validator(password):
        break


