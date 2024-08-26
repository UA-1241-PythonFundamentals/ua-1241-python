class Employee:

    """
    This is the Employee class.
    It represents an employee with a name and salary, and keeps track of the number of employees.
    """

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.increment_count()
    
    @classmethod
    def increment_count(cls):
        cls.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        print(cls.employee_count)
    
    def displayInformation(self):
        print (f"The employee {self.name} has a salary of {self.salary}$")


Petro = Employee("Petro",7000)
Sofia = Employee("Sofia", 5000)
Employee.get_employee_count()
Petro.displayInformation()
Sofia.displayInformation()

print(f"Base classes: {Employee.__bases__}")  # Базові класи
print(f"Class namespace: {Employee.__dict__}")  # Простір імен класу
print(f"Class name: {Employee.__name__}")  # Ім'я класу
print(f"Module name: {Employee.__module__}")  # Ім'я модуля
print(f"Documentation: {Employee.__doc__}")  # Документація класу