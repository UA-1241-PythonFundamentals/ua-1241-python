
class Polygon():
    '''This is Polygon class'''
    def area(self, *args):
        pass

class Rectangle(Polygon):
    '''This is Rectangle class'''
    def area(self, a, b):
        return a * b


r = Rectangle()
print(r.area(2, 4))
