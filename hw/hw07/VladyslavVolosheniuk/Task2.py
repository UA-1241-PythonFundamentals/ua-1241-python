#Task2. Write a program that calculates the area of a rectangle,
#triangle and circle
#(write three functions to calculate the area, and call them in the
#main program depending on the user's choice).
area1=input("Enter number 1.Rectangle, 2.Triangle or 3.Circle?: ")
if area1 == "1":
    length=int(input("Enter length:"))
    width=int(input("Enter width:"))
    result = length * width
    print(f"Area of a rectangle:'{result}'")
elif area1 == "2":
    a = float(input("Enter first side: "))  
    b = float(input("Enter second side: "))  
    c = float(input("Enter third side: "))  
    s = (a + b + c) / 2 
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of a Triangle is: %0.2f"%area)
elif area1 == "3":
    p = 3.14
    Radius= float(input("Enter radius of the given circle:"))
    area_circle = p * Radius * Radius
    print(f"Area of a circle: {area_circle}")



