def get_day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    if number in days:
        return days[number]
    elif number >= 8:
        raise ValueError("Number must be between 1 and 7.")
    else:
        raise TypeError("Invalid input. Please enter a number.")

def main():
    try:
        number = int(input("Enter a number (1-7) to get the corresponding day of the week: "))
        day = get_day_of_week(number)
        print(f"The day of the week is: {day}")
    except (ValueError, TypeError) as e:
        print(e)

if __name__ == "__main__":
    main()
