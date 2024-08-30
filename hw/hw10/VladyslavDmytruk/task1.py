class Polygon:
    def __init__(self, sides):
        self.sides = sides
    
    def number_of_sides(self):
        return self.sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        # Rectangle is a polygon with 4 sides
        super().__init__(4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage:
rect = Rectangle(5, 3)
print(f"Number of sides: {rect.number_of_sides()}")
print(f"Area of the rectangle: {rect.area()}")

