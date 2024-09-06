
def print_day(day):
    week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    print(week[int(day)-1])

def input_day():
    day = input("Enter number from 1 to 7: ")
    try:
        if int(day)<1 or int(day)>7:
            raise ValueError
        else:
            print_day(day)
    except ValueError:
        print("Error: Incorrect value.")
        input_day()

input_day()
    