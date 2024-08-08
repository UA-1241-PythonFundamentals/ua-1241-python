n = int(input("number:"))

#initial numbers
a, b = 0, 1
# container
mylist = []
while a <= n:
    mylist.append(a)
    a, b = b, a+b

print("Fibonacci numbers", mylist)