class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0 for _ in range(num_sides)]
    
    def input_sides(self):
        self.sides = [float(input(f"Enter length of side {i+1}: ")) for i in range(self.num_sides)]
    
    def display_sides(self):
        for i in range(self.num_sides):
            print(f"Side {i+1} is {self.sides[i]}")
class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
    def find_area(self):
        length, width = self.sides
        return length * width

rect = Rectangle()
rect.input_sides()
rect.display_sides()  
print(f"The area of the rectangle is {rect.find_area()} square units.")
