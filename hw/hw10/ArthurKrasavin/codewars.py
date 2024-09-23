import math
#Regular Ball Super Ball
class Ball:
    def __init__(self, ballType = "regular"):
        self.ballType = ballType

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ballType)
print(ball2.ballType)

#Color Ghost
class Ghost:
    import random
    colors = ["white", "yellow", "purple", "red"]
    def __init__(self, color = random.choice(colors)):
        self.color = color

ghost = Ghost()
print(ghost.color)

#Hard to Be a God
class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    pass

class Woman(Human):
    pass

def creation():
    l = []
    adam = Man("Adam")
    eve = Woman("Eve")
    l.append(adam)
    l.append(eve)
    return l

print(creation())

#Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getInfo(self):
        return f"{self.name}'s age is {self.age}"
    
person = Person("John", 34)
print(person.getInfo())

#Sphere
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round((4/3)*math.pi*math.pow(self.radius, 3), 5)
    def get_surface_area(self):
        return round(4*math.pi*math.pow(self.radius, 2), 5)
    def get_density(self):
        return round(self.mass/self.get_volume(), 5)
    
ball = Sphere(2, 50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())

#Dynamic classes
def change_class_name(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise Exception('Invalid class name. Must be name with alphanumeric chars (upper & lower letters plus ciphers), but starting only with upper case letter')
    return type(new_name, cls.__bases__, dict(cls.__dict__))

class Test:
    def hello(self):
        return "Hello from Test"

NewTest = change_class_name(Test, "NewTest")

# Перевірка:
print(NewTest().hello())  # Виведе: Hello from Test
print(NewTest.__name__)   # Виведе: NewTest