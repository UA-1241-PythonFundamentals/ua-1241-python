class Humman:
    homo = "Homo sapiens"
    def __init__(self,name):
        self.name =name
    def w_masage(self):
        print(f"Hello,{self.name}")
    
    @classmethod
    def s_infi(cls):
        return f" This class represents the species {cls.homo}"
    
    @staticmethod
    def masage():
        return "This is an arbitrary message."
   
persona = Humman("Ivan")
persona.w_masage()
print(Humman.s_infi())
print(Humman.masage())