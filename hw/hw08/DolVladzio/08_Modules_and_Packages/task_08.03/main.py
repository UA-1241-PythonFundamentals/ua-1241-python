if __name__ == "__main__":
    #_All import files
    from models.circle import *
    from models.triangle import *
    from models.rectangle import *
    #_User's interface
    print("- Select what are you want")
    print("- Area of Circle - C\n- Area of Triangle - T\n- Area of Rectangle - R")
    user_input = input("- ")
    #_Checking correct input
    if user_input == "C" or user_input == "c":
        #_Call in function
        circleArea()
    elif user_input == "T" or user_input == "t":
        #_Call in function
        triangleArea()
    elif user_input == "R" or user_input == "r":
        #_Call in function
        rectangleArea()
    else:
        print("- Incorrect input")