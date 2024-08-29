class Employee:
    c_employee = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: ${self.salary}")
    
    @classmethod
    def employee_count(cls):
        print(cls.employee_count)