"""Task 1"""
class Polygon:
    pass

class Rectangle(Polygon):

    def __init__(self):
        super().__init__()

    def square(sel, x, y):
        return x * y

rectangle = Rectangle()
side1 = float(input("Укажите первую сторону прямоугольника: "))
side2 = float(input("Укажите вторую сторону прямоугольника: "))
print(f"Площадь прямоугольника со сторона {side1} и {side2} равна: {rectangle.square(side1, side2)}")
