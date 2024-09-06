class Human:
    name = ""

    def __init__(self, name) -> None:
        self.name = name
        

    def welcome(self):
        return f"Hello, {self.name}!!!"
    
    @classmethod
    def species(cls):
        return "Homo sapiens, is usually defined as a large-brained bipedal primate"
    
    @staticmethod
    def atribute():
        return "Homo sapiens, is usually defined as a large-brained bipedal primate with a capacity for language and a knack for using complex tools."
