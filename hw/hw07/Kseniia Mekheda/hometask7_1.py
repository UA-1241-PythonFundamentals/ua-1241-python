# Task 1
def largest_num(a, b):
    """Finds the largest number between two given"""
    return a if a > b else b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(largest_num(a, b))

# Task 2
import math
def rectangle_square(a, b):
    """Needed arguments: width and height of a rectangle"""
    return a * b

# If you want to use the formula that requires an angle, enter 'a' as the last argument
def triangle_square(*args, symbol = " "):
    """Needed arguments: base and height OR two sides and an angle between them OR three sides"""
    # two sides and angle between them
    if symbol == "a":
        return round(0.5*args[0]*args[1]*math.sin(args[2]*(math.pi/180)), 0)
    # base and height
    elif len(args) == 2:
        return round(0.5*args[0]*args[1], 0)
    # three sides
    elif len(args) == 3:
        p = (args[0] + args[1] + args[2])/2
        return round(math.sqrt(p*(p - args[0])*(p - args[1])*(p - args[2])), 0)
    else:
        return "Fatal error"

def circle_square(r):
    """Needed arguments: radius"""
    return round(math.pi*r**2, 0)

print("Enter the figure, square of which you want to calculate:"
      "\n 1) rectangle - 'r' \n 2) triangle - 't' \n 3) circle - 'c'")

choise = input("Your choise. If you want to stop the work of this block of code, enter 'end': ")

while choise != 'end':
    match choise:
        case 'r':
            a = int(input("Enter height: "))
            b = int(input("Enter width: "))
            print("Square of rectangle:", rectangle_square(a, b))
            choise = input("Your choise. If you want to stop the work of this block of code, enter 'end': ")
        case 't':
            print("How would you like to calculate the square of the triangle?:"
                  "\n 1) base and height - 1 \n 2) two sides and angle between them - 2 \n 3) three sides - 3")
            option = int(input("Your choise: "))
            match option:
                case 1:
                    a = int(input("Enter base: "))
                    h = int(input("Enter height: "))
                    print("Square of triangle:", triangle_square(a, h))
                case 2:
                    a = int(input("Enter first side: "))
                    b = int(input("Enter second side: "))
                    angle = int(input("Enter angle (in degrees): "))
                    print("Square of triangle:", triangle_square(a, b, angle, symbol = "a"))
                case 3:
                    a = int(input("Enter first side: "))
                    b = int(input("Enter second side: "))
                    c = int(input("Enter third side: "))
                    print("Square of triangle:", triangle_square(a, b, c))
                case _:
                    print("Invalid symbol of choise.")
            choise = input("Your choise. If you want to stop the work of this block of code, enter 'end': ")
        case 'c':
            r = int(input("Enter radius: "))
            print("Square of circle:", circle_square(r))
            choise = input("Your choise. If you want to stop the work of this block of code, enter 'end': ")    
        case _:
            print("Invalid symbol of choice. Try again.")
            choise = input("Your choise. If you want to stop the work of this block of code, enter 'end': ")    

# Task 3
def caracters_included(word):
    return {symb : word.count(symb) for symb in set(word)}

word = input("Enter the word you want to analyse: ")
print(caracters_included(word))
