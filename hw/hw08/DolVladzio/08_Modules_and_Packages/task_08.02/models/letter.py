import re

def findLetter(user_password):
    if bool(re.search(r'[a-z]', user_password)) and bool(re.search(r'[A-Z]', user_password)):
         print("- At least 1 letter between A-Z: Ok\n- At least 1 letter between a-z: Ok")
    
    elif bool(re.search(r'[a-z]', user_password)) == False and bool(re.search(r'[A-Z]', user_password)) == False:
         print("- At least 1 letter between A-Z: None- At least 1 letter between a-z: None")
         
    else:
        print("- Your password don't have arrange A-Z or a-z. Try again") 
    