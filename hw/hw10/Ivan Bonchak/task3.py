class Employee:
    count =0
    def __init__(self,name,money):
        self.name=name
        self.money=money
        Employee.count +=1
    def info_emloi(self):
        print(f"Employee name {self.name} employee's salary {self.money}")
    @staticmethod
    def emplo_cout():
        print(f" Total number of employees:{Employee.count}")
    

emp1 = Employee("Ivan",3000)
emp2 = Employee("Olga",4000)
emp3 = Employee("OLER",5000)

emp1.info_emloi()
emp2.info_emloi()
emp3.info_emloi()
Employee.emplo_cout()

print(f"Базові класи: {Employee.__bases__}")  # Виводить базові класи, від яких успадковується клас Employee
print(f"Простір імен класу: {Employee.__dict__}")  # Виводить простір імен класу (атрибути та методи)
print(f"Назва класу: {Employee.__name__}")  # Виводить назву класу
print(f"Назва модуля: {Employee.__module__}")  # Виводить назву модуля, в якому визначено клас
print(f"Документація: {Employee.__doc__}")  # Виводить документацію класу (якщо є)