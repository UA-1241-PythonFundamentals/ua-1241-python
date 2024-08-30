class Employee:
    emp_count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1
    @classmethod
    def total_employees(cls):
        return f"Total number of employees: {cls.emp_count}"

    def employee_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"

emp1 = Employee('Emma', 86000.00)
emp2 = Employee('Alex', 92000.00)

print(emp1.employee_info())
print(emp2.employee_info())
print(Employee.total_employees())

print(f"Base classes: {Employee.__bases__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation: {Employee.__doc__}")