#_Task_1==============================
from time import sleep

x = range(11)

for n in x:
  print(f"Number {n} is {type(n)} and after convert to float type - {type(float(n))}")
  sleep(0.2)
#_Task_2==============================
from time import sleep
#_User input his number
while True:
    user_number_quantity = input("Write a quantity of numbers: ")
    #_Check if user's number is correct
    try:
        if (int(user_number_quantity) >= 0):
            break      
        elif (int(user_number_quantity) < 0):
            print("Incorrect input( Try again!")
    except :
        print("Incorrect input( Try again!")        
#=====================================
#_Creating Fibonacci number
count = 1
num_1 = 0
num_2 = 1
next_num = 0

while count <= int(user_number_quantity):
    next_num = num_1 + num_2
    
    print(next_num)
    
    num_1 = num_2
    num_2 = next_num
        
    count += 1
    sleep(0.15)
#_Task_3==============================
from time import sleep
#_User input his number
while True:
    user_factorial = input("Write a quantity of numbers: ")
    #_Check if user's number is correct
    try:
        if (int(user_factorial) >= 0):
            break      
        elif (int(user_factorial) < 0):
            print("Incorrect input( Try again!")
    except :
        print("Incorrect input( Try again!")        
#=====================================
#_Calculate factorial
count = 1        
result = 1

while count <= int(user_factorial):
    result *= count
    count += 1

print(f"{user_factorial}! = {result}")
#=====================================