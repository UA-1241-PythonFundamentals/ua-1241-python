import HW8_3
def main():
    print("Choose the shape to calculate the area:") 
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle") 
    choice = input("Enter the number of your choice (1/2/3): ") 
    if choice == '1': 
       a = float(input("Enter the length of the rectangle: ")) 
       b = float(input("Enter the width of the rectangle: ")) 
       area = HW8_3.rectangle_area(a, b) 
       print(f"The area of the rectangle is: {area}") 
    elif choice == '2': 
      a = float(input("Enter the base of the triangle: ")) 
      h = float(input("Enter the height of the triangle: ")) 
      area = HW8_3.triangle_area(a, h) 
      print(f"The area of the triangle is: {area}") 
    elif choice == '3':
      r = float(input("Enter the radius of the circle: ")) 
      area = HW8_3.circle_area(r) 
      print(f"The area of the circle is: {area}") 
    else: 
      print("Invalid choice. Please select 1, 2, or 3.") 
