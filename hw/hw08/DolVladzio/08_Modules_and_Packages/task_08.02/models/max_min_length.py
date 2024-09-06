def maxMinLength(user_password):    
    if len(user_password) >= 6 and len(user_password) <= 16:
        print("- Length: Ok!")        
    elif len(user_password) > 16:
        print("- Incorrect. So long")
    elif len(user_password) < 6:
        print("- Incorrect. So short")