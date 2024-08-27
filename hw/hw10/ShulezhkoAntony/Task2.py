class Human:
    species = "Homosapiens" 
    def __init__(self, name):
        self.name = name     
    def welcome_message(self):
        print(f"Welcome, {self.name}!")    
    @classmethod
    def species_info(cls):
        # Class method that returns information about the species
        return f"We are of the species {cls.species}."
    @staticmethod
    def arbitrary_message():
        # Static method that returns an arbitrary message
        return "This is an arbitrary message from the Human class."

person1 = Human("Alice")
person2 = Human("Bob")
person1.welcome_message()
person2.welcome_message()  

print(Human.species_info())

# Call the static method
print(Human.arbitrary_message())
