"""Task 1"""


def lagest_number(lst):
    """This function returns the largest number of two receiving from user"""
    lst.sort()
    print(lst)
    return print(f"Наибольшее из введённых чисел: {lst[1]}")


user_input = input("Пожалуйста, введите два числа через запятую: ")
if "," in user_input:
    user_input = user_input.replace(" ", "").split(",")
    if user_input[0].isdigit() and user_input[1].isdigit():
        user_input = list(map(int, user_input))
        lagest_number(user_input)
    else:
        print("Вы ввели не числа.")
else:
    print("Пожалуйста, введите числа именно через запятую.")
