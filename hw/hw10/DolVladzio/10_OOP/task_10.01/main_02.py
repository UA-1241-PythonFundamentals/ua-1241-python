class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcomeMessage(self):
        print(f"Welcome, {self.name}")

    def typeSpices(self):
        print(f'It\'s a species of "{self.species}"')

    @staticmethod
    def randomMessage():
        return "Static message"

if __name__ == "__main__":
    user_input = input("Write your name: ")
    
    person = Human(user_input)
    person.welcomeMessage()
    print(person.randomMessage())
