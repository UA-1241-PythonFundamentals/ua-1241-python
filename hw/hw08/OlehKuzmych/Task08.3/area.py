from math import pi
from math import pow


def rectangle():
  """This function calculate the area of rectangle"""
  a = float(input("Enter a: "))
  b = float(input("Enter b: "))
  return a * b

def triangle():
  """This function calculate the area of triangle"""
  a = float(input("Enter a: "))
  h = float(input("Enter h: "))
  return round( (a * h) / 2, 2 )

def circle():
  """This function calculate the area of circle"""
  r = float(input("Enter r: "))
  return round( pi * pow(r, 2), 2 )


if __name__ == "__main__":
    print("You need to call main.py")
