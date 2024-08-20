import re
p=input("Enter password: ",)

def f(p):
    if len(p)<=6 or len(p)>=16: 
        return False  
    if not (re.search("[0-9]",p) and re.search("[@#$]",p)):
        return False
    if not (re.search("[a-z]",p) and re.search("[A-Z]",p)):
        return False
    return True

while not f(p):
    p=input("Password is incorrect,enter the correct password: ",)
else:
    print("Welcome!")
    
