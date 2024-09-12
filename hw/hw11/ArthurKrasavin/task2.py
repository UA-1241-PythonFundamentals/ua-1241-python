class MyError(Exception):
    def __init__(self, data):
        self.data = data

def day_check(number):
    day_dict = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
    try:
        number = int(number)
        if number >= 1 and number <= 7:
            return f"{number} is {day_dict[number]}"
        else:
            raise MyError("The number you entered is not a day number")
    except (ValueError, TypeError):
        return "Please, enter the number"
    except MyError as e:
        return e

day = input("Enter the day number: ")
print(day_check(day))