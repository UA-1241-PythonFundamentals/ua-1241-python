def square_rectangle(a,b):
    """The function calculates the area of a rectangle.
    Input a, b - the sides of the rectangle"""
    return f"Square of a rectangle with sides {a} and {b} = {a*b}"

def square_triangle(a,b,c):
    """The function calculates the area of a triangle.
    Input a, b, c - the sides of the triangle"""
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        s=(p*(p-a)*(p-b)*(p-c))**(1/2)
        s=round(s,2)
        return f"Square of a triangle with sides {a}, {b} and {c} = {s}"
    else:
        return ("It is not a triangle")
    
def square_circle(r):
    """The function calculates the area of a circle.
    Input r - the radius of the circle"""
    if r>0:
        s=3.14*r*r
        s=round(s,2)
        return f"Square of a circle with radius {r} = {s}" 

def program():
    """Shape selection function"""
    shape = input("Choose shape (rectangle/triangle/circle): ").lower()
    if shape == "rectangle":
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        print(f"Square: {square_rectangle(a, b)}")
    elif shape == "triangle":
        a = float(input("Side a: "))
        b = float(input("Side b: "))
        c = float(input("Side c: "))
        print(f"Square: {square_triangle(a, b, c)}")
    elif shape == "circle":
        r = float(input("Radius: "))
        print(f"Square: {square_circle(r)}")
    else:
        print("Invalid!")

# print (square_rectangle(3, 6))
# print (square_triangle(2,4,5))
# print (square_circle(2))
program()