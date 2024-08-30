# Task 1
class Polygon:
    pass


class Rectangle(Polygon):
    def __init__(self):
        super().__init__()

    def square(self, x, y):
        return x * y


rect = Rectangle()
print(rect.square(2, 4))

# Task 2


class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def display_welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species_info(cls):
        return f"The species is {cls.species}."

    @staticmethod
    def static_message():
        return "This is an arbitrary message."


bob = Human('Bob')

print(bob.display_welcome_message())
print(Human.get_species_info())
print(Human.static_message())
