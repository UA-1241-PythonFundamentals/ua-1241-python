
import uuid

class Human():
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        return f"Hello, {self.name}"

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def random_message() -> str:
        return str(uuid.uuid4())


human = Human("Oleh")
print(human.sayHello())
print(human.species())
print(Human.random_message())
