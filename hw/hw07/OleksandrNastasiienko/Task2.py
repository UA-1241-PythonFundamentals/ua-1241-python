def rectangle(a, b):
    area = a * b
    return area

def triangle(b, h):
    area = 1/2 * b * h
    return area

def circle(r):
    area = 3.14 * r**2
    return area

figure = input("Choose the figure for area calculation ( rectangle | triangle | circle ): ")

if figure == "rectangle":
    a = input("Input first side value: ")
    b = input("Input secont side value: ")
    area = rectangle(int(a), int(b))
    print("Area of your rectangle is: ", area)
elif figure == "triangle":
    b = input("Input triangle base value: ")
    h = input("Input triangle heights value: ")
    area = triangle(int(b), int(h))
    print("Area of your triangle is: ", area)
elif figure == "circle":
    r = input("Input circle radius value: ")
    area = circle(int(r))
    print("Area of your circle is: ", area)
else:
    print("Wrong figure type. Please try again")