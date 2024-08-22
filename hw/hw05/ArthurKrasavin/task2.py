x = int(input("Enter the number: "))
first, second, third = 0, 1, 1
print(first)
print(second)
print(third)
y = 0
while y < x:
    y = second + third
    print(y) 
    second = third
    third = y
    