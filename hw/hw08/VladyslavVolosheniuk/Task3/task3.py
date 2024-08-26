#Task3.
#Write a program that calculates the area of a rectangle S=a*b, the area of a
#triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
#another module in which we ask the user the area of which figure he wants to calculate.
#(To perform the task, you need to import the math module, and from it the
#pow() function and the value of the variable pi, and module, which contains
#three functions for finding areas, into the main program. The basic logic of the
#program is executed in the main module).

calculates = input("Enter shape number for calculates area (1.rectangle/2.triangle/3.circle?): ")
import formuls
    
if calculates == "1":
    a=float(input("Enter a: "))
    b=float(input("Enter b: "))
    s=formuls.area_rectangle(a,b)
    print(f"The area of a rectangle {s}")
else:
    print("Enter only number")
if calculates == "2":
    a=float(input("Enter a: "))
    h=float(input("Enter h: "))
    s=formuls.area_triangle(a,h)
    print(f"The area of a triangle {s}")
if calculates == "3":
    r=float(input("Enter r: "))
    s=formuls.area_circle(r)
    print(f"The area of a circle {s}") 