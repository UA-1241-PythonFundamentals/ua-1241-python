import json


class Employee():

    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count = Employee.count + 1

    @staticmethod
    def get_total_employees() -> int:
        return Employee.count

    def get_employee(self):
        return json.dumps({
                "name": self.name,
                "salary": self.salary,
                })    

empl1 = Employee("Sam", 100)
empl2 = Employee("Mike", 200)

print(empl1.get_employee())
print(empl2.get_employee())

print(f"Total count employees: {Employee.get_total_employees()}")

print()
print()

print(f"{'Base classes:   ':<5} {Employee.__base__}")
print(f"{'Class namespace:':<5} {Employee.__dict__}")
print(f"{'Class name:     ':<5} {Employee.__name__}")
print(f"{'Module name:    ':<5} {Employee.__module__}")
print(f"{'Class doc:      ':<5} {Employee.__doc__}")