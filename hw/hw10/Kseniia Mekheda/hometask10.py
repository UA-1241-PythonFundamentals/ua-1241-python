# Task 1
class Polygon:
    def __init__(self, sides_quantity):
        self.num_sides = sides_quantity
        self.sides = self.sides_input()

    def sides_input(self):
        print("Enter sides of polygon: ")
        sides = [float(input()) for i in range(0, self.num_sides)]
        return sides
    
class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def square(self):
        return self.sides[0] * self.sides[1]
    

a = Polygon(5)
b = Rectangle()

print(b.square())

# Task 2
class Human:
    def __init__(self, name):
        self.name = name
    
    def welcome_message(self):
        print(f"Welcome, {self.name}!")
    
    @property
    def species():
        return "Homosapiens"
    
    @staticmethod
    def message():
        return "Hello!"

# Task 3
class Employee:
    counter = 0
    def __init__(self, name, salary):
        self.employee_name = name
        self.employee_salary = salary
        counter += 1
    
    def total(self):
        print(f"Total quantity of workers now is {self.counter}")

    def info(self):
        print(f"Worker name: {self.employee_name} \nWorker salary: {self.employee_salary}")

print(Employee.__base__, '\n', Employee.__dict__, '\n', Employee.__name__, '\n', Employee.__module__, '\n',
      Employee.__doc__)

    
    
