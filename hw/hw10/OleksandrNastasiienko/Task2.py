class Human:

    species = "Homosapiens" 

    def __init__(selfe, name):
        selfe.name = name
        print(f"Hello {name}")

    @classmethod
    def homo(cls):
        return f"Humans are all {cls.species}"
    
    @staticmethod
    def ping():
        return f"Let it be peice"

Human("Alex")
print(Human.homo())
print(Human.ping())