from formuls import rectangle, triangle, circle

def main():
    area = input("Which area would you like to calculate?")
    
    if area.lower() == 'rectangle':
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        print(f"The area of the recctangle is: {rectangle(a, b)}")
        
    elif area.lower() == 'triangle':
        h = float(input("Enter the height of the triangle: "))
        a = float(input("Enter the base of the triangle: "))
        print(f"The area of the triangle is: {triangle(h, a)}")
        
    elif area.lower() == 'circle':
        r = float(input("Enter the radius of the circle: "))
        print(f"The area of the circle is: {circle(r)}")
        
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
