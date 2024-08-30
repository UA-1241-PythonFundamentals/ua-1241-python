a=int(input('Enter number 1: ',))
b=int(input('Enter number 2: ',))
def larg(a,b):
    'The function returns the largest number of two numbers'
    return max(a,b)
print('Largest number:',larg(a,b))