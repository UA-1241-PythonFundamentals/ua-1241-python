def get_day(number):
    days = {
        0:"Monday",
        1:"Tuesday",
        2:"Wednesday",
        3:"Thursday",
        4:"Friday",
        5:"Saturday",
        6:"Sunday"
    }

    return days[number]

def input_info():
    try:
        number = int(input("Write number: "))
    except ValueError:
        print("You need to enter a number")
        input_info()
    else:
        print(get_day(number%7))

if __name__ == "__main__":
    input_info()