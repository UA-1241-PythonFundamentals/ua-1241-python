class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def employee_info(self):
        print(f"- Name: {self.name}\n- Salary: {self.salary}")

    def total_employees_count(cls):
        print(f"Total Employees: {cls.total_employees}")

if __name__ == "__main__":
    emp1 = Employee("Vladzio", 100000)
    emp2 = Employee("Max", 60000)
    
    emp1.employee_info()
    emp2.employee_info()

    Employee.total_employees

    print(f"Base classes: {Employee.__base__}")
    print(f"Namespace: {Employee.__dict__}")
    print(f"Class name: {Employee.__name__}")
    print(f"Module: {Employee.__module__}")
    print(f"Documentation: {Employee.__doc__}")