class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total_employees_count(cls):
        print(f"Total Employees: {cls.total_employees}")

if __name__ == "__main__":
    emp1 = Employee("Alice", 50000)
    emp2 = Employee("Bob", 60000)
    
    emp1.display_info()
    emp2.display_info()
    
    Employee.total_employees_count()
    
    print(f"Base classes: {Employee.__base__}")
    print(f"Namespace: {Employee.__dict__}")
    print(f"Class name: {Employee.__name__}")
    print(f"Module: {Employee.__module__}")
    print(f"Documentation: {Employee.__doc__}")
