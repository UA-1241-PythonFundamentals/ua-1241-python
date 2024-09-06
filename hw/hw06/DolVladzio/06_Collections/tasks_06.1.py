#_Task_1
user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#============================
# - a)
i = 0

while i < len(user_list):
    if (user_list[i]) % 2 == 0:
        print(f"{user_list[i]} is divisible by 2")
        i += 1
    else:
        i += 1
        continue
#============================
# - b)
i = 0

while i < len(user_list):
    if (user_list[i] % 2 == 0) % 3 == 0:
        print(f"{user_list[i]} is odd and divisible by 3")
        i += 1
    else:
        i += 1
        continue
#============================    
# - c)
i = 0

while i < len(user_list):
    if (user_list[i] % 2 != 0) and (user_list[i] % 3 != 0):
        print(f"{user_list[i]} aren't divisible by 2 and 3")
        i += 1
    else:
        i += 1
        continue    
#============================