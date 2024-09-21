import random as rd
class Human:
    name = ''
    def __init__(self,name):
        self.name = name
    
    def greeting(self):
        print(f"Hello {self.name}")
    def who_it_is(self):
        print('It is a species homosapien')
    @staticmethod
    def rand_message(num):
        print(num*rd.randint(0,5))
john = Human("John")

john.greeting()
john.rand_message('W')