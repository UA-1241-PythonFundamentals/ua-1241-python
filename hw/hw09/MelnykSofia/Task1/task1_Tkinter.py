import tkinter as tk
from random import randint

# Створюємо головне вікно
root = tk.Tk()
root.title("Guess the number")  # Назва вікна
root.configure(bg="#013220") # Змінюємо колір фону
root.geometry("400x400")  # Розмір вікна (ширина x висота)

# Генеруємо випадкове число
random_num = randint(1, 100)
step = 0  # Лічильник спроб

# Додаємо мітку (label)
label = tk.Label(root, text="Guess the number!", font=("Arial", 20))
label.pack(pady=30)  # Розміщуємо мітку в центрі з відступом 20 пікселів

# Додаємо текстове поле (entry)
entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=10)

# Функція для перевірки числа
def guess_number():
    global step
    try:
        my_num = int(entry.get())  # Отримуємо число з текстового поля і перетворюємо на int
    except ValueError:
        label.config(text="Please enter a valid number!")
        return
    
    step += 1  # Збільшуємо кількість спроб
    
    if my_num > random_num:
        label.config(text=f"Attempt {step}: {my_num} is greater than the number.")
    elif my_num < random_num:
        label.config(text=f"Attempt {step}: {my_num} is less than the number.")
    else:
        label.config(text=f"You win! The number was {random_num}.")
        return  # Якщо користувач вгадав, завершення функції

    if step >= 10:  # Якщо використано всі 10 спроб
        label.config(text=f"You lose! The number was {random_num}.")
        entry.config(state='disabled')  # Блокуємо текстове поле після завершення гри

# Додаємо кнопку (button)
button = tk.Button(root, text="Check the number", font=("Arial", 14), command=guess_number)
button.pack(pady=10)

# Запускаємо головний цикл програми
root.mainloop()
