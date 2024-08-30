class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def employee_count(cls):
        return f"Total number of employees: {cls.total_employees}"

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)

print(Employee.employee_count())
print(emp1.display_info())
print(emp2.display_info())

print("Base classes:", Employee.__bases__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
