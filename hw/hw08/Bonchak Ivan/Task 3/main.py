import areas
def main():
    print("Choose the shape you want to calculate the area for:\n1. Rectangle\n2. Triangle\n3. Circle")

    choice = input("Your choice (1/2/3): ")

    if choice == '1':
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        print(f"The area rectangle is: {areas.rectangle_a(a, b)}")

    elif choice == '2':
        h = float(input("Enter the height h: "))
        a = float(input("Enter the length of the base a: "))
        print(f"The area  triangle is: {areas.triangle_a(h, a)}")

    elif choice == '3':
        r = float(input("Enter the radius r: "))
        print(f"The area circle is: {areas.circle_area(r)}")

    else:
        print("Invalid !")

if __name__ == "__main__":
    main()

