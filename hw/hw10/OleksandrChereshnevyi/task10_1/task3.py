from task2 import Human

class Employee(Human):
    '''Employee test class'''
    static_counter = 0
    static_list = []
    salary = 0.0

    def __init__(self, name, salary) -> None:
        super().__init__(name)
        self.salary = salary
        Employee.static_counter += 1
        Employee.static_list.append(self)

    def __str__(self) -> str:
        return f"Name: {self.name} Salary: {self.salary} "
    
    @staticmethod
    def counter():
        return Employee.static_counter
    
    @staticmethod
    def print_all():
        for i in Employee.static_list:
            print(i)


p1 = Employee("Alex", 1000)
p2 = Employee("Alex2", 2000)
p3 = Employee("Alex3", 3000)

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

Employee.print_all()