class Polygon:
    def area(self,*args):
        pass

class Rectangle(Polygon):
    def area(self, a,b):    
        return a*b
    def side_sqwear(self,side):
        return side**2
        
r= Rectangle()
print("Площа прямокутника:",r.area(2,4))
print("Квадрат сторони а:",r.side_sqwear(2))
print("Квадрат сторони b:",r.side_sqwear(4))