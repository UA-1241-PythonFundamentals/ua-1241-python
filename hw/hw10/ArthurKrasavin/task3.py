class Employee:
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    @classmethod
    def print_employee_count(cls):
        print(f"Total number of employees: {cls.employee_count}")
    
    def display_employee_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")
        
emp1 = Employee("John", 50000)
emp2 = Employee("Jane", 60000)

emp1.display_employee_info()
emp2.display_employee_info()

Employee.print_employee_count()

print("\nClass Information:")
print(f"Base class: {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")
