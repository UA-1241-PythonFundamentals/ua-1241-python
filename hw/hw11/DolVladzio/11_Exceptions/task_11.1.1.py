#========================================
try:
    user_input = int(input("- Write your age: "))

    if user_input <= 0:
        raise Exception

    elif user_input > 0 and user_input <= 100:
        if user_input % 2 == 0:
            print(f"- {user_input} is even age")
        else:
            print(f"- {user_input} is odd age")

    else:
        print(f"\n- Age {user_input} so big")
    
except ValueError as error_info:
    print(f"\n- Incorrect input({error_info})")
except Exception:
    print("\n- Number can't be less or equal than 0")
#========================================