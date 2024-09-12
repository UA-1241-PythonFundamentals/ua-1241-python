import math

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
   return math.pi * radius ** 2

def main():
    print("Choose the shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = int(input("Enter your choice (1/2/3): "))
    
    if choice == 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {rectangle_area(length, width)}")
    elif choice == 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"The area of the triangle is: {triangle_area(base, height)}")
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {circle_area(radius)}")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

main()
