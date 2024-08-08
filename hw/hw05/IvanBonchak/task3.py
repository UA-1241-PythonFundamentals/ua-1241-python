n = int(input("n:"))
factorial = 1
for a in range(1,n+1):
    factorial *= a

print( f"Factorial {n}! = {factorial}")