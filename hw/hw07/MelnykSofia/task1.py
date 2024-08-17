def simile(num1, num2):
    """returns the largest number of two numbers"""
    if num1==num2:
        return ("The numbers are the same")
    return max(num1,num2)
print(simile(2,4))
print(simile(7,3))
print(simile(5,5))