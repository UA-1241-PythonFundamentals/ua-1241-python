from math import pi,pow
def area(f):
    if f==1:
        a=float(input("Enter side 1: ",))
        b=float(input("Enter side 2: ",))
        return a*b
    elif f==2:
        a=float(input("Enter the base of the triangle: ",))
        h=float(input("Enter the height of the triangle: ",))
        return 0.5*a*h
    elif f==3:
        r=float(input("Enter radius: ",))
        return round(pi*(pow(r,2)),1)