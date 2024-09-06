import re
print("Create a password. It must contain:")
print("\t- At least 1 letter between [a-z] and 1 letter between [A-Z]")
print("\t- At least 1 number between [0-9]")
print("\t- At least 1 character from [$#@]")
print("\t- Minimum length 6 characters")
print("\t- Maximum length 16 characters")

password = input("\nEnter your password: ")
pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$"

if re.match(pattern, password):
    print("Password is valid.")
else:
    print("Password is invalid.")