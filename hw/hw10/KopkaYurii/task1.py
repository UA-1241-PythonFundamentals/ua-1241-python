class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        super().__init__(num_sides=4)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
rect = Rectangle(5, 3)
print("The area of the rectangle is:", rect.area())
