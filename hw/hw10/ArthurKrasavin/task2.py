class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species(cls):
        return "This species is Homo sapiens."

    @staticmethod
    def random_message():
        return "Humans are capable of amazing things!"
    
person = Human("John")
print(person.welcome())
print(Human.species())
print(Human.random_message())