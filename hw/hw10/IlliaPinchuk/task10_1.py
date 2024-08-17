class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    rect = Rectangle(10, 20)
    print(f"The area of the rectangle is: {rect.area()}")
