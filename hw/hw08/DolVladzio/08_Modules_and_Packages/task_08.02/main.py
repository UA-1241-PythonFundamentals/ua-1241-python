if __name__ == "__main__":
    from models.letter import *
    from models.number import *
    from models.character import *
    from models.max_min_length import *

    user_password = input("Write your password: ")
    #_Call in function
    findLetter(user_password)    
    #_Call in function
    findNumber(user_password)
    #_Call in function
    findCharacter(user_password)
    #_Call in function
    maxMinLength(user_password)