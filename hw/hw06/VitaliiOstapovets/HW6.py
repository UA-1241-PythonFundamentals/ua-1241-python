#Task1
list_a = []
list_b = []
list_c = []
for a in range (1,10):
    if a % 2 ==0 and a % 2 ==0:
        list_a.append(a)
print(f"Even numders that are divisible by 2 {list_a}")

for b in range (1,10):
    if b % 2 ==1 and b % 3 == 0:
        list_b.append(b)
print(f"Odd numbers, which are divisible by 3 {list_b}")
for c in range (1,10):
    if c % 2 != 0 and c % 3 != 0:
        list_c.append(c)
print(f"Numbers that are not divisible by 2 and 3 {list_c}")

#Task2
auntefication = False
while auntefication == False:
    login = input("Input login")
    if login == 'First':
        print("Hello First")
        auntefication = True
    else:
        print("Error:Unknown login ")
