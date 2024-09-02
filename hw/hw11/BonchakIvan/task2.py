class Hw11T2:
    def __init__(self):
        self.day = {
            1:"Понеділок",
            2:"Вівторок",
            3:"Середа",
            4:"Четвер",
            5:"Пятниця",
            6:"Субота",
            7:"Неділя",
        }
        self.get_day()

    def get_day(self):
        while True:
            try:
                namber = int (input("Ведіть число від 1-7 "))
                if 1 <= namber <=7:
                    print(f"Цей день тижня: {self.day[namber]}")
                    break
                else:
                    print("Помилка: Введіть число від 1 до 7.")
                    
   
            except ValueError:
                print("Помилка: Введене значення не є числом. Спробуйте ще раз.")
            except Exception as e:
                print(f"Сталася несподівана помилка: {e}")

start = Hw11T2()
