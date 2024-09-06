class Poligon:
    def __init__(self,s):
        self.s=s
    def info (self):
        print(f"The polygon you're working with has {self.s} sides.")
class Area(Poligon):
    def __init__(self,w,h):
        self.w=w
        self.h=h
        super().__init__(4)
    def area(self):
        return self.h*self.w

resr = Area(14,12)
resr.info()
print(f"The surface area of the rectangle measures  {resr.area()}")