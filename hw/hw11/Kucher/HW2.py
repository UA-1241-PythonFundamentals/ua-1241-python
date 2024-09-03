def get_day_of_week():
    try:
        number = int(input("Введіть число від 1 до 7: "))

        days_of_week = {
            1: "Понеділок",
            2: "Вівторок",
            3: "Середа",
            4: "Четвер",
            5: "П'ятниця",
            6: "Субота",
            7: "Неділя"
        }
        if 1 <= number <= 7:
            print(f"Введене число відповідає: {days_of_week[number]}")
        elif number >= 8:
            print("Число більше або дорівнює 8. Введіть число від 1 до 7.")
            #АБо додати num % 7 і зациклити 
        else:
            print("Число повинно бути в межах від 1 до 7.")
    except ValueError:
        print("Будь ласка, введіть ціле число.")
#call
get_day_of_week()