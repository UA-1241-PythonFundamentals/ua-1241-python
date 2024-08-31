#Task_2
from math import pi
#==========================================
def main():
    #_Functions
    def circleArea():
        r = input("Write radius of circle: ")
        
        if float(r) <= 0:
            print("Incorrect input")
            
        elif float(r) > 0:
            circle_area = pi * (float(r) ** float(2))
            print(f"Area of circle: {circle_area}cm3")

        else:
            print("Incorrect")
    
    def triangleArea():
        triangle_base = input("Write a base of triangle: ")
        
        triangle_height = input("Write a height of triangle: ")
        
        if float(triangle_base) <= 0 and float(triangle_height) <= 0:
            print(f"You have some mistakes:\n- Base of triangle can't be {triangle_base} only > 0\n- Hiegth of triangle can't be {triangle_height}, only > 0 but < base")

        elif float(triangle_height) < float(triangle_base):
            triangle_area = (1/2) * float(triangle_base) * float(triangle_height)
            print(f"Area of triangle: {triangle_area}cm2")
            
        else:
            print(f"- Hiegth of triangle can't be {triangle_height}, only < base")
    
    def rectangleArea():
        rectangle_width = input("Write width of rectangle: ") 
        
        rectangle_lendth = input("Write lendth of rectangle: ") 
        
        if float(rectangle_width) <= 0 and float(rectangle_lendth) <= 0:
            print(f"You have some mistakes:\n- Width of rectangle can't be {rectangle_width} only > 0\n- Lendth of rectangle can't be {rectangle_lendth}, only > 0, but < width")

        elif float(rectangle_lendth) < float(rectangle_width):
            rectangle_area = float(rectangle_lendth) * float(rectangle_width)
            print(f"Area of rectangle: {rectangle_area}cm2")
            
        else:
            print(f"- Lendth of rectangle can't be {rectangle_lendth}, only < rectangle of width")
    
    #_User input
    print("Select what are you want")
    print("Area of Circle - C\nArea of Triangle - T\nArea of Rectangle - R")
    user_input = input("$_")

    if user_input == "C" or user_input == "c":
        circleArea()
    elif user_input == "T" or user_input == "t":
        triangleArea()
    elif user_input == "R" or user_input == "r":
        rectangleArea()
    else:
        return "Incorrect input"

main()
#==========================================