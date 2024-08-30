# Task 2. Write a program that calculates the ares of a rectangle,
# triangle and circle

# (write three functions to calculate the area, and call them in the
#  main program depending on the users choice).

def rectangle(a, b):
    return a * b

def triangle(b, h):
    return b * h * 0.5

def circle(h):
    return h**2 * 3.14

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
        c = int(input("Enter c: "))
        print(f"Result of circle= {circle(c)}")