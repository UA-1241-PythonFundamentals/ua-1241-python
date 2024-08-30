from math import pi, pow


class CalculateArea:

    def rectangle(self, width, height):
        print(width * height)
        return width * height

    def triangle(self, height, base):
        print(0.5*height*base)
        return 0.5*height*base

    def circle(self, radius):
        print(round(pi*pow(radius, 2), 2))
        return round(pi*pow(radius, 2), 2)
