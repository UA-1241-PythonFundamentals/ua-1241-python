class Polygon:
    def __init__(self,sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self,a,b):
        super().__init__(sides=4)
        self.a = a
        self.b = b
    def area_rt(self):
        self.product = self.a*self.b
        return self.product

