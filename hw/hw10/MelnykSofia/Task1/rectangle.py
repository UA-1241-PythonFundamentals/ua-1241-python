from polygon import Polygon

class Rectangle(Polygon):

    """Class Rectangle finds the square of the rectangle"""

    def __init__(self,a,b):
        super().__init__(2) #посилаємося на Polygon і одразу вказуємо, що сторін 4
        self.a = a
        self.b = b

    def findArea(self):
        s = self.a * self.b 
        return (f"Square regtangle is: {s}")
