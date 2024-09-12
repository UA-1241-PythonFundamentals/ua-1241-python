"""I. Ball-super-ball"""
class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

    def __str__(self):
        return f"{self.ball_type}"

"""II. Color-ghost"""
import random

lst = ["white", "yellow", "purple", "red"]
class Ghost(object):
    def __init__(self):
        self.object = object
        self.color = random.choice(lst)

first = Ghost()
print(first.color)

"""III. Basic-subclasses-Adam-and-Eve"""
class God:
    pass

class Human(God):
    pass

class Man(Human):
    pass

class Woman(Human):
    pass


def god():
    paradise = [Man(), Woman()]
    return paradise

paradise = god()
print(isinstance(paradise[0], Man))

"""IV. Classy-classes"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info=f"{name}s age is {age}"

"""V. Building Spheres"""
from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        # print(self.radius)
        return self.radius

    def get_mass(self):
        # print(self.mass)
        return self.mass

    def get_volume(self):
        # print(round(self.radius**3 * (4/3 * pi), 5))
        return round(self.radius**3 * (4/3 * pi), 5)

    def get_surface_area(self):
        # print(round(4 * pi * self.radius**2, 5))
        return round(4 * pi * self.radius**2, 5)

    def get_density(self):
        # print(round(self.mass / self.get_volume(), 5))
        return round(self.mass / self.get_volume(), 5)


ball = Sphere(2,50)
ball.get_radius() #->       2
ball.get_mass() #->         50
ball.get_volume() #->       33.51032
ball.get_surface_area() #-> 50.26548
ball.get_density() #->      1.49208

ball = Sphere(0.39,33.04)
ball.get_density()

"""VI. Dynamic Classes"""
class MyClass:
    pass


def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
        # print(new_name.__name__)
    else:
        raise
