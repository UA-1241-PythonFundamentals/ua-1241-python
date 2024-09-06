from random import randint


number = randint(0, 100)
print("Привет! Я загадал число и предлагаю его отгадать.")
print("У вас 10 попыток. После каждой попытки я буду чуть-чуть подсказывать :)")

for attempt in range(1, 11):
    print(f"Попытка №: {attempt}")
    user_number = int(input("Укажите Ваше число: "))

    if user_number == number:
        print("Супер! Вы угадали число! Я искренне Вас поздравляю!")
        break
    elif user_number < number:
        print("Я загадал число, которое болье Вашего")
    elif user_number > number:
        print("Я загадал число, которое меньше Вашего.")

    if attempt == 10:
        print("К сожалению, это была последняя попытка и Вы не угадали число.")
        print(f"Загаданным числом было: {number}")

