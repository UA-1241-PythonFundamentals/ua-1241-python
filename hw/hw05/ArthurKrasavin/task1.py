from random import randint
l = [randint(0, 100) for _ in range(10)]
for i in range(len(l)):
    print(l[i])
    l[i] = float(l[i])
print(l)