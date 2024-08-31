import re

def findCharacter(user_password):
    if bool(re.search(r'[$#@]', user_password)):
         print("- At least 1 character between $, # or @: Ok")
    
    elif bool(re.search(r'[$#@]', user_password)) == False:
         print("- At least 1 character $, # or @: None")
         
    else:
        print("- Your password don't have character S, #, or @. Try again") 