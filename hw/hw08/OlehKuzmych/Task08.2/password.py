import re

def is_valid(password) -> bool:
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$", password):
        return True
    return False

if __name__ == "__main__":
    print(f"password Passw@rd1 is {is_valid('Passw@rd1')}.")
    print(f"password 123456789 is {is_valid('123456789')}.")
    print(f"password aaaaabbbb is {is_valid('aaaaabbbb')}.")