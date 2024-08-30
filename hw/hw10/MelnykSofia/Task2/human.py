class Human:
    name = "Petro"
    def __init__(self, name):
        self.name = name

    # def inputName(self):
    #     self.name = input("Enter your name: ")

    def displayGreet(self):
        print (f"Hello, {self.name}!")
    
    @classmethod
    def homosapies(cls,name):
        cls.name = name
        print(f"Name: {cls.name}, Species: Homosapiens")
    
    @staticmethod
    def message():
        print (f"Ти знаєш, що ти — людина. Ти знаєш про це чи ні?")
    
Anna = Human("Anna")
Anna.displayGreet()
Human.homosapies("Sofia")
Human.message()