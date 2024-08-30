import re
password=input("Enter password: ")

password_requirements="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[$#@]).{8,16}$"
result=re.match(password_requirements,password)
print(result)

