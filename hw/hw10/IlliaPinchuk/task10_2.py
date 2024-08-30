class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Hello, {self.name}! Welcome to the world of {self.species}")

    @classmethod
    def species_info(cls):
        return f"Species: {cls.species}"

    @staticmethod
    def random_message():
        return "Arbitrary static message"

if __name__ == "__main__":
    person = Human("John")
    person.welcome_message()
    print(Human.species_info())
    print(Human.random_message())
