#_Task_2
user_login = ["First"]

user_input = input("Write your password: ")

i = 0

while i < len(user_login):
    if user_input == user_login[i]:
        print("Welcome)")
        break
    else:
        print("Incorrect input")
        break
#=====================================   