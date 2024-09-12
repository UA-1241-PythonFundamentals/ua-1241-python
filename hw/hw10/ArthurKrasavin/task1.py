class Polygon:
    def __init__(self, sides_count):
        self.sides_count = sides_count

class Rectangle(Polygon):
    def __init__(self, a, b):
        super().__init__(sides_count=4)
        self.a = a
        self.b = b
    
    def area(self):
        return self.a * self.b
    
rectangle = Rectangle(8, 4)
print("Area of your rectanlge is:", rectangle.area())