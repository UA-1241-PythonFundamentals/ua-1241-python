int_list = [1, 2, 3, 4, 5]  
float_list = []  

for num in int_list:
    float_list.append(float(num))

print("Original integer list:", int_list)
print("Converted float list:", float_list)