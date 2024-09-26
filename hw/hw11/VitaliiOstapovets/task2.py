def main():
    day_input = input("Plese input day week:")
    check_day(day_input)
def check_day(number):
    day_week = None
    try:
        if  0 < int(number)< 8:
            day_week = number
        else: 
            raise ValueError
        
    except ValueError as e:
        print("Incorect day week")
    except Exception as er:
        er("Hi hihihih")
    list_days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"]
    if  day_week != None:
        print(list_days[int(day_week)-1])

if __name__ == "__main__":
    main()