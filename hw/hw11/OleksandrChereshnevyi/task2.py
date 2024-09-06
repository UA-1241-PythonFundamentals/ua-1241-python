def day_helper():
    list_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    try:
        number =  int(input("Enter number: "))
        if number <= 0 or number >= 8:
            raise ValueError("That is not an availably number!")
        return list_days[number - 1]
    except ValueError as e:
        print(e)
    except:
        print("Something went wrong")

print(day_helper())