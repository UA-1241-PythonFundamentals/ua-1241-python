from re import findall

password = input("Password: ")

def check_password(password):
    if len(findall(r"(.*[A-z]+.*)", password)) == 0:
        print("You have to use lower and uper letter")
        return False
    if len(findall(r"(.*[0-9]+.*)", password)) == 0:
        print("You have to use numbers")
        return False
    if len(findall(r"(.*[@#$]+.*)", password)) == 0:
        print("You have to use one of this @#$")
        return False
    if 16 < len(password):
        print("Password is so long")
        return False
    if 5 > len(password):
        print("Password is so small")
        return False
    print("password is correct")
    return True

print(check_password(password=password))
