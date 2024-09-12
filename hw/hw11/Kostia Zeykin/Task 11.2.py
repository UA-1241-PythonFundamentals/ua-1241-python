"""Task 1"""
"""В этом задании я не понимаю, как пройти последний тест - проверку принадлежности 
функции check_positive классу MyError"""
class MyError(Exception):
    pass


def check_positive(number):
    try:
        number = float(number)
        if number >= 0:
            return f"You input positive number: {float(number)}"
        else:
            raise MyError
    except ValueError:
            return "Error type: ValueError!"
    except MyError:
        return f"You input negative number: {float(number)}. Try again."

"""Task 2"""
def check_odd_even(number):
    try:
        if number % 2 == 0:
            return "Entered number is even"
        else:
            return "Entered number is odd"
    except:
        return "You entered not a number."

"""Task 3"""
def divide(numerator, denominator):
    try:
        return f"Result is {numerator / denominator}"
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    except TypeError:
            return "Value Error! You did not enter a number!"

"""Task 4"""
class InputError(Exception):
    def __init__(self, data):
        self.data = data

def check(text):
    if not isinstance(text, str):
        raise InputError("Type text error")
    elif len(text) < 3:
        raise InputError("Short text error")
    elif len(text) > 15:
        raise InputError("Long text error")
    else:
        return "True"

def test_input(text):
    try:
        print(check(text))
    except InputError as e:
        print(e.data)

"""Task 5"""
import re


def check(login):
    sample = r"^(admin|employee)(.+)(\d+)$"
    check_login = re.match(sample, login.lower())

    if check_login:
        return f"True"
    else:
        raise ValueError(f"incorrect login '{login}'")

from random import choices
from string import ascii_letters, digits

letters_and_digits = choices(ascii_letters, k=5)
letters_and_digits.extend(choices(digits, k=5))
incorrect_login = ''.join(letters_and_digits)
print(incorrect_login)
try:
    if check(incorrect_login):
        print("checked successfully")
except ValueError as e:
    print(str(e) == f"incorrect login '{incorrect_login}'")

"""Task 6"""
def check_age(age):
    if age <= 0:
        raise ValueError("Incorrect age")

answer = False
while not answer:
    try:
        age = int(input())
        check_age(age)
    except ValueError as e:
        pass
    else:
        print(age)
        answer = True
