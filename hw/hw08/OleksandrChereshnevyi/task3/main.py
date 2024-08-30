from models import *

choise = ""

while(choise != "q"):
    choise = input("Please enter:\n"
                   + "a. Area of rectangle\n"
                   + "b. Area of triangle\n" 
                   + "c. Area of circle\n"
                   + "Your choise: ")
    if (choise == "a"):
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        print(f"Result of rectangle = {rectangle(a, b)}")
    elif (choise == "b"):
        b = int(input("Enter base: "))
        h = int(input("Enter h: "))
        print(f"Result of triangle= {triangle(b, h)}")
    elif (choise == "c"):
        c = int(input("Enter r: "))
        print(f"Result of circle= {circle(c)}")
