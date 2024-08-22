x = int(input("Enter the number: "))
fact = 1
if x == 0:
    print(1)
else:
    for i in range(1, x):
        fact = (fact*(i+1))
print(fact)