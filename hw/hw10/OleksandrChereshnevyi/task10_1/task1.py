class Polygon:
    sides = []

    def __init__(self, no_sides):
        self.sides = [0 for i in range(no_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)}: "))for i in range(len(self.sides))]

    
class Triangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def square(self):
        return self.sides[0] * self.sides[1]

