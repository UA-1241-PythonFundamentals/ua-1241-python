import re
password = input("Enter password for validation: ")
if len(password) >= 6 and len(password) <= 16 and re.match("[a-z]+[A-Z]+\d+[$@#]+", password):
    print("Your password is great!:)")
else:
    print("Password doesn`t match some of the requirements that are listed below: "
          "\n 1) At least 1 letter between [a-z] and 1 letter between [A-Z]."
          "\n 2) At least 1 number between [0-9]."
          "\n 3) At least 1 character from [#@]."
          "\n 4) Minimum length 6 characters."
          "\n 5) Maximum length 16 characters.")