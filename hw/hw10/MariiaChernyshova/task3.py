class employee:
    number =0

    def __init__(self,n=0,s=0):
        self.name = n
        self.salary = s
        employee.number+=1

    def total_number():
        print(f"Total number of employees: {employee.number}")

    def employee_info(self):
        print(f"Employee name: {self.name}, salary: {self.salary}")

emp1 = employee("Ida",10000)
emp2 = employee("Paul",20000)
emp3 = employee("Anders",30000)

employee.total_number()
emp2.employee_info()

print(employee.__base__)
print(employee.__dict__)
print(employee.__name__)
print(employee.__module__)
print(employee.__doc__)
