class MyCustomError(Exception):
    def __init__(self):
        pass



def check_number(number):
    if number%2 == 0:
        print("number is even")
    else:
        print("number is odd")

def input_number():
    try:
        number = int(input("Write number: "))
        if number < 0:
            raise MyCustomError
        else: check_number(number)
    except MyCustomError:
        print("Age cannot be negative")


if __name__ == "__main__":
    input_number()