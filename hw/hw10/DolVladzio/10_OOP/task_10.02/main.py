#_1_Ball-super-ball
class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type
#_2_Color-ghost
class Ghost(object):
    def __init__(self):
        import random
        self.color = random.choice(["white", "yellow", "purple", "red"])
# _3_Basic-subclasses-Adam-and-Eve
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
# _4_Classy-classes
class Person:
    def __init__(self, name,age):
        self.info=f"{name}s age is {age}"
# _5_Building Spheres
import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return (self.radius)

    def get_mass(self):
        return (self.mass)

    def get_volume(self):
        V = (4/3) * math.pi * (self.radius ** 3)

        return (round(V, 5))

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)

        return (round(surface_area, 5))

    def get_density(self):
        density = self.mass / self.get_volume()

        return (round(density, 5))

ball = Sphere(2, 50)

#_6_Dynamic Classes
def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise Exception('Invalid')
    cls.__name__ = new_name