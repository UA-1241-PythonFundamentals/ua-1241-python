class Employee:

    '''Create an employee class. Each employee has characteristics such as name
and salary. The class should have a counter that calculates the total number of
employees, as well as a method that prints the total number of employees and a
method that displays information about each employee in particular, namely the
name and salary.'''

    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def full_info(self):
        print(f"Employee name: {self.name}, Employee salary: {self.salary}")

    @classmethod
    def total_emp(cls):
        print(f"Total number of employees: {cls.counter}")


emp1 = Employee("Alex", 3000)
emp2 = Employee("Sergey", 7000)

emp1.full_info()
emp2.full_info()

Employee.total_emp()
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__) 