class Polygon():
    def __init__(self, sides):
        self.sides=sides
class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)
rectangle=Rectangle(5,4)
rectangle.area()

class Human():
    def __init__(self, name):
        self.name=name
    def greeting(self):
        print("Hello ", self.name)
    def homosapiens(self):
        print("Homosapiens")
    @staticmethod
    def message():
        print("Hello")
John=Human("John")
John.greeting()
John.homosapiens()
John.message()

class Employee():
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
        Employee.counter+=1
    counter=0

    def printemployeecount(self):
        print(self.counter)
    def printnameandsalary(self):
        print(self.name + ": "+ str(self.salary))
John=Employee("John",1000)
John.printemployeecount()
John.printnameandsalary()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

