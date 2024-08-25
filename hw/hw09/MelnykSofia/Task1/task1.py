from random import randint

random_num=randint(1,100)
step=0

while step<10:
    step+=1
    my_num=int(input("Enter number: "))
    if my_num>random_num:
        print(f"The attempt {step}. Your number {my_num} is greater than my number")
    elif my_num<random_num:
        print(f"The attempt {step}. Your number {my_num} is less than my number")
    elif my_num==random_num:
        print (f"You win!")
        break
else:
    print("You lose!")    
