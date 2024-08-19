import module
from math import pow
from math import pi

figure=input("What area do you want to find?: ")
if figure=="circle":
    radius=input("Enter radius: ")
    radius=int(radius)
    module.area_circle(radius)
elif figure=="rectangle":
    length=input("Enter length: ")
    width=input("Enter width: ")
    length=int(length)
    width=int(width)
    module.area_rectangle(length, width)
elif figure=="triangle":
    base=input("Enter base: ")
    height=input("Enter height: ")
    base=int(base)
    height=int(height)
    module.area_triangle(height, base)
else:
    print("Wrong shape")


