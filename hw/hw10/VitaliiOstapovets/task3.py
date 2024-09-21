class Employees:
    __count_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        __count_employees += 1
    def __del__(self):
        __count_employees -= 1
    @classmethod
    def num_empl(cls):
        print(f"Count employees is {cls.__count_employees}")
    def info_emp(self):
        print(f"Name is {self.name}")
        print(f"Salary is {self.salary}")
    @classmethod   
    def all_info_clas(cls):
        print(f"Base classes: {cls.__base__}")
        print(f"Class namespace: {cls.__dict__}")
        print(f"Class name: {cls.__name__}")
        print(f"Module name: {cls.__module__}")
        print(f"Documentation: {cls.__doc__}")     

Employees.all_info_clas()