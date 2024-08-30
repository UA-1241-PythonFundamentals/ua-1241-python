n = int(input("Enter the limit for Fibonacci Sequence presentation: "))
n1 = 0
n2 = 1
nn = n1 + n2
print("Fibonacci Sequence:")
print(n1)
print(n2)
while nn <= n:
    print(nn)
    n1 = n2
    n2 = nn
    nn = n1 + n2