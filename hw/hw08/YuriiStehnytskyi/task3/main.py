from calculations import area_of_rectangle, area_of_triangle, area_of_circle

def main():
    print("Choose the figure to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter the number of your choice: ")
    
    if choice == '1':
        a = float(input("Enter the length of rectangle: "))
        b = float(input("Enter the width of rectangle: "))
        print(f"The area of the rectangle is: {area_of_rectangle(a, b)}")
    
    elif choice == '2':
        h = float(input("Enter the height of the triangle: "))
        a = float(input("Enter the base of the triangle: "))
        print(f"The area of the triangle is: {area_of_triangle(h, a)}")
    
    elif choice == '3':
        r = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {area_of_circle(r)}")
    
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
