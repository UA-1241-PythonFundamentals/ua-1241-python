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
    else:
        raise ValueError("The number must be between 1 and 7.")

def main():
    try:
        number = int(input("Enter a number (1-7): "))
        day = get_day_of_week(number)
        print(f"The day corresponding to number {number} is {day}.")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
