from math import pi

def circleArea():
    #_User's data
    r = input("- Write radius of circle: ")
    #_Checking correct data
    #_1_Showing some mistakes(if it'll be:))  
    if float(r) <= 0:
        print("- Incorrect input")
    #_2_Showing result(If all will be alright:))        
    elif float(r) > 0:
        circle_area = pi * (float(r) ** float(2))
        print(f"- Area of circle: {circle_area}cm3")
    #_3_Showing another some mistakes(if it'll be:))  
    else:
        print("- Incorrect")