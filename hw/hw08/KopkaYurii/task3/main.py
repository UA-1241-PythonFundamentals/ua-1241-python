from area_calculations import rectangle_area, triangle_area, circle_area

def main():
    choice = input("Which area would you like to calculate? (1 - Rectangle, 2 - Triangle, 3 - Circle): ")
    
    if choice == '1':
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        print(f"The area of the rectangle is: {rectangle_area(a, b)}")
        
    elif choice == '2':
        h = float(input("Enter the height of the triangle: "))
        a = float(input("Enter the base of the triangle: "))
        print(f"The area of the triangle is: {triangle_area(h, a)}")
        
    elif choice == '3':
        r = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {circle_area(r)}")
        
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
