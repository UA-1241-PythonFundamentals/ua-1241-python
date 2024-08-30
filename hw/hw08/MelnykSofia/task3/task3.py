shape=input("Enter shape (rectangle/triangle/circle(): ").lower()

import functions

if shape == "rectangle":
    a=float(input("Enter a: "))
    b=float(input("Enter b: "))
    s=functions.area_rectangle(a,b)
    print(f"The area of a rectangle {s}")
if shape == "triangle":
    a=float(input("Enter a: "))
    h=float(input("Enter h: "))
    s=functions.area_triangle(a,h)
    print(f"The area of a triangle {s}")
if shape == "circle":
    r=float(input("Enter r: "))
    s=functions.area_circle(r)
    print(f"The area of a circle {s}")
