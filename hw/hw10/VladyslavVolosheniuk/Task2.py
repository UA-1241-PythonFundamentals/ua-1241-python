import random
class Human:
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name
    def welcome(self):
        print(f"Welcome {self.name}")
    @classmethod
    def get_species(cls):
        return f"This species is {cls.species}."
    @staticmethod
    def random_message():
        messages = [
            "Hello world!",
            "You are amazing",
            "How are you?",
            "Have a good day!",
            "Belive in your self!" 
        ]
        return random.choice(messages)
person1 = Human("Alex")
person2 = Human("Martin")

person1.welcome(), person2.welcome()

print(Human.get_species())
print(Human.random_message())


