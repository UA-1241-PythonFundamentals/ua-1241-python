list1, list2, list3 = [], [], []
for i in range(1, 11):
    if (i%2==0):
        list1.append(i)
    elif (i%3==0):
        list2.append(i)
    elif (i%2>0 and i%3>0):
        list3.append(i)

print("Even numbers that are divisible by 2: ", list1)
print("Odd numbers which are divisible by 3: ", list2)
print("Numbers that are not divisible by 2 and 3:", list3)