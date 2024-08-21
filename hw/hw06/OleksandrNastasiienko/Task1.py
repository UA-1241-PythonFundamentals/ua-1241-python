even = []
odd = []
other = []
for x in range(10):
    if x % 2 == 0:
        even.append(x)
    elif x % 3 == 0:
        odd.append(x) 
    else:
        other.append(x)
print("even = ", even)
print("odd = ", odd)
print("other = ", other)