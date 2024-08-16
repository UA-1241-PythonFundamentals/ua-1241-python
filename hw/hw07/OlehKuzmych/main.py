#Task 1
def func_max(x, y):
  """This function returns the maximum of two numbers"""
  if x > y:
    return x
  else:
    return y


print(func_max.__doc__)
print(func_max(1, 2))
print(func_max(-1, 10))


#Task 2
def rectangle(a, b):
  """This function returns the area of rectangle"""
  return a * b


def circle(r):
  """This function returns the area of circle"""
  return 3.14 * (r**2)


def triangle(a, h):
  """This function returns the area of triangle"""
  return (a * h) / 2


while 1 == 1:
  option = float(
      input("Calcuate shape area (1-rectangle, 2-circle, 3-triangle): "))
  if option not in [1.0, 2.0, 3.0]:
    print("Wrong option")
  else:
    if option == 1.0:
      print(rectangle.__doc__)
      a = float(input("Enter a: "))
      b = float(input("Enter b: "))
      print(rectangle(a, b))
      break
    elif option == 2.0:
      print(circle.__doc__)
      r = float(input("Enter r: "))
      print(circle(r))
      break
    elif option == 3.0:
      print(triangle.__doc__)
      a = float(input("Enter a: "))
      h = float(input("Enter h: "))
      print(triangle(a, h))
      break
    break


#Task 3
def func_calc_symb(text):
  """This function returns the number of symbols in the text"""
  result = {}
  for symb in text:
    if symb in result:
      result[symb] += 1
    else:
      result[symb] = 1
  return result


print(func_calc_symb.__doc__)
print(func_calc_symb("hello"))
print(func_calc_symb("hellllo"))
