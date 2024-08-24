import random
from gift import *

attempt = 10
generated_number = random.randint(1, 100)
#print(generated_number)


while attempt > 0:
    entered_num = int(input("Enter number: "))

    if entered_num < generated_number:
        print("the generated number is more")
    elif entered_num > generated_number:
        print("the generated number is less")
    else:
        showCardWinner()
        break 
            
    attempt -= 1
else:
    showCardLosser()

