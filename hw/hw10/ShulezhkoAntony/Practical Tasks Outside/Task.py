#I. Ball-super-ball
class Ball:
  def __init__(self, ballType="regular"):
    self.ballType = ballType

ball1 = Ball();
ball2 = Ball("super");

print(ball1.ballType)
print(ball2.ballType)

#II. Color-ghost
class Ghost:
  def __init__(self):
    import random
    self.color = random.choices(["white", "yellow", "purple", "red"])

ghost = Ghost()
print(ghost.color)

#III. Basic-subclasses-Adam-and-Eve
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

#IV. Classy-classes
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  @property
  def info(self):
    return f"{self.name}s age is {self.age}"

stats = Person("John", 34)
print(stats.info)

#V. Building Spheres
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
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(volume, 5)
    
    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)
    
    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)

ball = Sphere(2,50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())

#VI. Dynamic Classes

import types
import re

def change_class_name(cls, new_name):
    # Check if the new name starts with an uppercase letter and is alphanumeric
    if not re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        raise ValueError("The class name must start with an uppercase letter and contain only alphanumeric characters.")
    return types.new_class(new_name, cls.__bases__, {}, lambda ns: ns.update(cls.__dict__))
class MyClass:
    pass

try:
    NewClass = change_class_name(MyClass, "NewClassName")
    print(NewClass.__name__)
except ValueError as e:
    print(e)

try:
    InvalidClass = change_class_name(MyClass, "1InvalidName")
    print(InvalidClass.__name__)
except ValueError as e:
    print(e)
