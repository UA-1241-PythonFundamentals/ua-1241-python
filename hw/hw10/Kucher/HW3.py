class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def print_total_employees(cls):
        print(f"Скільки тих: {cls.count}")

    def display_employee_info(self):
        print(f"І'мя: {self.name}, Зарплата: {self.salary}")

emp1 = Employee("Брайан", 50000)
emp2 = Employee("Торето", 60000)

# Display information about each employee
emp1.display_employee_info()
emp2.display_employee_info()

# Скільки тих
Employee.print_total_employees()

# Display information about the Employee class
print(f"Base classes of Employee: {Employee.__base__}")
print("__")
print(f"Class namespace of Employee: {Employee.__dict__}")
print("__")
print(f"Class name: {Employee.__name__}")
print("__")
print(f"Module name: {Employee.__module__}")
print("__")
print(f"Documentation: {Employee.__doc__}")