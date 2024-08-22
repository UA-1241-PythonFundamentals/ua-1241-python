import calculations

print("Choose type of figure, which square you want to calculate: "
      "\n Rectangle - 'r' \n Triangle - 't' \n Circle - 'c'")

choise = input("Enter your choise here If you want to finish your calculations enter 'end': ")

while choise != 'end':
    match choise:
        case 'r':
            a = int(input("Enter first side: "))
            b = int(input("Enter second side: "))
            print(f"Square of the rectangle {a} x {b} equals to {calculations.rectangle_square(a, b)}")
            choise = input("Enter your choise here If you want to finish your calculations enter 'end': ")
        case 't':
            a = int(input("Enter base of triangle: "))
            h = int(input("Enter height of triangle: "))
            print(f"Square of the triangle with base {a} and height {h} equals to {calculations.triangle_square(a, h)}")  
            choise = input("Enter your choise here If you want to finish your calculations enter 'end': ") 
        case 'c':
            r = int(input("Enter radius of the circle: "))
            print(f"Square of the circle with radius {r} equals to {calculations.circle_square(r)}")
            choise = input("Enter your choise here If you want to finish your calculations enter 'end': ")
        case _:
            print("Ooops, wrong symbol :(")
            choise = input("Enter your choise here If you want to finish your calculations enter 'end': ")
else:
    print("Bye-Bye :)")