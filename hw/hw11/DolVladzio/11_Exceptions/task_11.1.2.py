#========================================
week_days = ["Monday", 
            "Tuesday", 
            "Wednesday", 
            "Thursday", 
            "Friday", 
            "Saturday", 
            "Sunday"]
#========================================
try:
    user_input = int(input("- Write a number of day you are want: "))

    if user_input > 7 or user_input < 1:
        print(f"\n- Incorrect input(can't be less than 1 or bigger than 7)")
    else:
        print(f"\n- {user_input} day is - {week_days[(user_input - 1)]}")

except ValueError:
    print("\n- Incorrect input(must be number)")
finally:
    print("- End of program")
#========================================