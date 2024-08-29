import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    max_try = 10

    print(f"Вгадай число від 1 до 100. Є {max_try} спроб, щоб вгадати його.")

    for num in range(max_try):
        while True:
            user_input = input("Введіть ваше число: ")            
            if user_input.isdigit():
                guess = int(user_input)
                if 1 <= guess <= 100:
                    break
                else:
                    print("Не число в діапазоні від 1 до 100.")
            else:
                print("Не дійсне число.")
        
        # Порівнюємо введене число з загаданим
        if guess != number_to_guess:
            print("Загадане число інше.")   
        else:
            return (f"Вітаємо! Ви вгадали число {number_to_guess} з {num + 1} спроб!")
        
        # Виводимо кількість залишених спроб
        print(f"Залишилось спроб: {max_try - num - 1}")
    
    print(f"Вибачте, але ви не вгадали число. Загадане число було {number_to_guess}.")

guess_the_number()