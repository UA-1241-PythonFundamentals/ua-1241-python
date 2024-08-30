class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species_info(cls):
        return f"Ніфіга не поняв, але схоже це cls мало бути {cls.species}."

    @staticmethod
    def arbitrary_message():
        return "Статік хрінь."

person = Human("Alice")
print(person.welcome_message())  
print(Human.species_info())     
print(Human.arbitrary_message()) 