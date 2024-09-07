"""Task 1"""
class Polygon:
    pass

class Rectangle(Polygon):

    def __init__(self):
        super().__init__()

    def square(self, x, y):
        return x * y

rectangle = Rectangle()
side1 = float(input("Укажите первую сторону прямоугольника: "))
side2 = float(input("Укажите вторую сторону прямоугольника: "))
print(f"Площадь прямоугольника со сторонами {side1} и {side2} равна: {rectangle.square(side1, side2)}")

"""Task 2"""
class Human:
    spec = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Добро пожаловать, {self.name}")

    @classmethod
    def species(cls):
        print(f"Этот класс создан для {cls.spec}")

    @staticmethod
    def message():
        print("Это произвольное сообщение.")


user_name = input("Представьтесь, пожалуйста: ")
user_name = Human(user_name)
user_name.greeting()
user_name.species()
user_name.message()
