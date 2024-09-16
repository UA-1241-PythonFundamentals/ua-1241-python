import random

magic_num = random.randint(0,100)

for i in range(0,10):
    dif_num = int(input("Input number: "))
    if dif_num == magic_num:
        print("Greeying, wery good!")
        break
    elif dif_num > magic_num:
        print("The number is greater!")
    elif dif_num < magic_num:
        print("The number is less!")
    else:
        print("Error")
    print(f"you have {9-i} more attempts" )
        
print("You used all the attempts but unfortunately you didn't guess")