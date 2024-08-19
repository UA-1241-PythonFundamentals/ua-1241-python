def largest_number(a, b):
    """Function returns the largest number of two numbers"""   
    return max (a, b)

print(largest_number(95, 80))

#Calculate the area of figures

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    import math
    return math.pi * radius ** 2

def program():
    shape = input("Choose shape (rectangle/triangle/circle): ").lower()
    if shape == "rectangle":
        length = float(input("Length: "))
        width = float(input("Width: "))
        print(f"Area: {area_rectangle(length, width)}")
    elif shape == "triangle":
        base = float(input("Base: "))
        height = float(input("Height: "))
        print(f"Area: {area_triangle(base, height)}")
    elif shape == "circle":
        radius = float(input("Radius: "))
        print(f"Area: {area_circle(radius)}")
    else:
        print("Invalid choice!")

program()
#
def characters(text):
    dictionary={}
    for i in text:
        if i in dictionary:
            dictionary[i]=dictionary[i]+1
        else:
            dictionary[i]=1
    print(dictionary)

word=input("Enter word: ")

characters(word)