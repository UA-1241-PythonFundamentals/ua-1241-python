# Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

# Color Ghost
class Ghost(object):
    def __init__(self):
        import random
        self.color = random.choice(["white", "yellow", "purple", "red"])

# Basic subclasses - Adam and Eve
class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name="Adam"):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name="Eve"):
        super().__init__(name)

def God():
    return [Man(), Woman()]

# Classy Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
    
# Building Spheres
import math

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        # Volume of a sphere = 4/3 * pi * r^3
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(volume, 5)
    
    def get_surface_area(self):
        # Surface area of a sphere = 4 * pi * r^2
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)
    
    def get_density(self):
        # Density = mass / volume
        density = self.mass / self.get_volume()
        return round(density, 5)
    
# Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise Exception('Invalid')
    cls.__name__ = new_name

