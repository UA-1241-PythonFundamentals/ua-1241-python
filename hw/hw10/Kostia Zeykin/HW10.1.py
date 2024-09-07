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

"""Task 3"""
class Employee:
    """Class about employees: surname and salary"""
    quantity = 0
    def __init__(self, surname, salary):
        self.surname = surname
        self.salary = salary
        Employee.quantity +=1

    def about_employee(self):
        print(f"Сотрудник с фамилией {self.surname} получает зарплату {self.salary}")

    @staticmethod
    def total_count_of_employee():
        print(f"Общее кол-во сотрудников равно {Employee.quantity}")


employee1 = Employee("Ivanov", 1000)
employee2 = Employee("Petrov", 2000)
employee3 = Employee("Sidorov", 3000)

employee1.about_employee()
employee2.about_employee()
employee3.about_employee()

print(f"Базовый класс: {Employee.__bases__}")
print(f"Пространство имён класса: {Employee.__dict__}")
print(f"Имя модуля: {Employee.__name__}")
print(f"Документация по классу: {Employee.__doc__}")
