n=7491
product = 0
# Converting integer to string 
num = str(n) 
# Traversing the string 
for i in num: 
    product = product + int(i) 
print(product) 
print(" ")

print(str(num)[::-1])
#start:stop:step. When you pass -1 as step, the start point goes to the end and stop at the front.
print(" ")

txt = '7491'
x = sorted(txt)
print(x)