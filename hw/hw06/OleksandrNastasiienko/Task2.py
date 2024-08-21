mylogin = tuple("First")
while True:
    login = tuple(input("Enter your login: "))
    if mylogin == login:
        print("Welcome in the system")
        break
    else:
        print("Wrong login, please try again")