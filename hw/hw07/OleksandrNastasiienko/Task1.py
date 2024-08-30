def largeN(a, b):
    """Function that returns 
    the largest number of two
    numbers."""
    if a>b:
        res = a
        return res
    else:
        res = b
        return res
    
a = input("Enter first value for compair: ")
b = input("Enter second value for compare: ")

print(largeN(a, b))