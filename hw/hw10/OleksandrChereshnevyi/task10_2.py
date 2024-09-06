# Practical Tasks
import random
import math

# I. Ball-super-ball
class Ball(object):
    ball_type = ""

    def __init__(self, name = "regular") -> None:
        self.ball_type = name

# II. Color-ghost
class Ghost(object):
    colors = ["white", "yellow", "purple", "red"]
    color = ""

    def __init__(self) -> None:
        self.color = str(self.colors[random.randint(0, 3)])

# III. Basic-subclasses-Adam-and-Eve
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

# IV. Classy-classes
class Person:
    def __init__(self, name, age):
        self.info= f"{name}s age is {age}"

# V. Building Spheres
class Sphere(object):
    def __init__(self, radius, mass) -> None:
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(self.radius**3 * math.pi * 4 / 3, 5)
    
    def get_surface_area(self):
        return round(self.radius**2 * 4 * math.pi, 5)
    
    def get_density(self):
        return round(self.mass / self.get_volume(), 5)

# VI. Dynamic Classes
def class_name_changer(cls, new_name):
    cls.__name__ = new_name
