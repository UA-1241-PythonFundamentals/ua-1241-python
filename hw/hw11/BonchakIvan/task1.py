class HW11:
    def __init__(self):
        self.age=0
        
    def get_age(self):
        while True:
            try:
                self.age= int(input("Введіть  вік: "))
                if self.age < 0:
                    raise ValueError ("Вік не може бути  відємне число ")
                elif self.age % 2 == 0:
                    return f"Ваш вік {self.age} є парним числом."
                else:
                    return f"Ваш вік {self.age} є  не парним числом."
        
            
            except ValueError as e:
                print(f"Error: {e} \n Спробуйте  ще раз ")

            except Exception as e:
                print(f" Стався несподіваний Error: {e} \n Спробуйте  ще раз ")
    

start = HW11()
result =start.get_age()
print(result)