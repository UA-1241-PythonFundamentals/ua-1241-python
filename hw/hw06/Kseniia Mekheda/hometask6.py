# Task 1
numbers = range(1, 11)
even_nums, odd_by_three, not_two_and_three = [], [], []
for num in numbers:
    if num % 2 == 0:
        even_nums.append(num)
    elif num % 3 == 0:
        odd_by_three.append(num)
    elif num % 2 != 0 and num % 3 != 0:
        not_two_and_three.append(num)

print("Even numbers list:", even_nums, 
      "\nOdd and divisible by 3 list:", odd_by_three, 
      "\nNot divisible by 2 and 3:", not_two_and_three)

# Task 2
usr_login = input("Please, enter your login: ")

while usr_login != "First":
    print("Error: Invalid user login. Try again")
    usr_login = input(" Enter your login: ")
else: 
    print(f"Hello, {usr_login}! How is your day going?")
    