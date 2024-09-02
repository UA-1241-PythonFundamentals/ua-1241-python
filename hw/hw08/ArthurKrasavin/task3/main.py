import area
print("\nWhich area do you want to calculate?")
print("1 - Area of rectangle")
print("2 - Area of triangle")
print("3 - Area of circle")
print("0 - Exit")
answer = int(input("Enter your choice: "))

while answer !=0:
    if answer == 1:
        a = int(input("\nEnter a side: "))
        b = int(input("Enter b side: "))
        print("\nArea of your rectangle is ", area.rectangle(a,b))
    elif answer == 2:
        l = int(input("\nEnter the lengths of the base: "))
        h = int(input("Enter height: "))
        print("\nArea of your triangle is ", area.triangle(h,l))
    elif answer == 3:
        r = int(input("\nEnter the radius of your circle: "))
        print("\nArea of your circle is: ", area.circle(r))
    else:
        print("\nChoose correct option")
    
    print("\nWhich area do you want to calculate?")
    print("1 - Area of rectangle")
    print("2 - Area of triangle")
    print("3 - Area of circle")
    print("0 - Exit")
    answer = int(input("Enter your choice: "))
print ("Bye!")