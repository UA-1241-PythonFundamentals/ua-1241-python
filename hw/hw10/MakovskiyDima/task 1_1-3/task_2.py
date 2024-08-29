class Human:

    def __init__(self, name):
        self.name = name
        self.say_welcome()

    def say_welcome(self):
        print(f"Welcome {self.name}")

    @classmethod
    def info_about_species():
        return "Homosapiens"
    
    @staticmethod
    def get_message():
        return "welcome"