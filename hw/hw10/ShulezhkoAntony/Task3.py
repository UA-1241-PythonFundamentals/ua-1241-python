class Employee:
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.employee_count}")

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

emp1.display_employee_info()
emp2.display_employee_info()

Employee.display_total_employees()
print(f"Base classes: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}") 
