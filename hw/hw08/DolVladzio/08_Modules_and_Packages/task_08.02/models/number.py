import re

def findNumber(user_password):
    if bool(re.search(r'[0-9]', user_password)):
         print("- At least 1 number between 0-9: Ok")
    
    elif bool(re.search(r'[0-9]', user_password)) == False:
         print("- At least 1 number between 0-9: None")
         
    else:
        print("- Your password don't have arrange 0-9. Try again") 
    