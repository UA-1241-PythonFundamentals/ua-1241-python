name = input()
class human:
    sp = "Homosapiens"
    def __init__(self,n):
        self.name = n
        print(f'Hello, {self.name}!')
   
    @classmethod
    def species(cls):
        return f"You are {human.sp}." 
    
    @staticmethod
    def message():
        return "Arbitary message"


human(name)
print(human.species())
print(human.message())