import re

def is_valid_password(password):
    '''Перевіряє пароль на всі символи'''
    # Перевірка довжини пароля
    count = 0
    for char in password:
        count += 1
    if count < 6 or count > 16:
        return False
    
    # Перевірка наявності хоча б однієї маленької літери
    has_lower = False
    for char in password:
        if 'a' <= char <= 'z':
            has_lower = True
            break
    if not has_lower:
        return False
    
    # Перевірка наявності хоча б однієї великої літери
    has_upper = False
    for char in password:
        if 'A' <= char <= 'Z':
            has_upper = True
            break
    if not has_upper:
        return False
    
    # Перевірка наявності хоча б однієї цифри
    has_digit = False
    for char in password:
        if '0' <= char <= '9':
            has_digit = True
            break
    if not has_digit:
        return False
    
    # Перевірка наявності хоча б одного спеціального символу з [$#@]
    has_special = False
    for char in password:
        if char in "$#@":
            has_special = True
            break
    if not has_special:
        return False
    
    return True

password = input("Enter your password: ")

if is_valid_password(password):
    print("Password is valid")
else:
    print("Password is invalid.")