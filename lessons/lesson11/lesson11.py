# print("dbsvkd" #SyntaxError: '(' was never closed



# a = int(input("a:"))





# Program to handle multiple errors with one except statement
# try:
#     a = int(input("Enter your number: "))
#     if a < 4:
#         b = a/(a-3) # throws ZeroDivisionError for a = 3
#         print(b)
#     if a >= 4:
#         print("Value of b = ", b) # throws NameError
#     # note that braces () are necessary here for multiple exceptions
# except(ZeroDivisionError, NameError, ValueError):
#     print("Error Occurred and Handled")


# print("end")
# run = True
# while run:
#     try:
#         a = int(input("Enter your number: "))
#         if a == 0:
#             run = False
#         if a < 4:
#             b = a/(a-3) # throws ZeroDivisionError for a = 3
#             print(b)
#         if a >= 4:
#             print("Value of b = ", b) # throws NameError
#         # note that braces () are necessary here for multiple exceptions
#     except ZeroDivisionError:
#         print("ZeroDivisionError!")
#     except NameError:
#         print("NameError!")
#     except ValueError:
#         print("ValueError")
#     except:
#         print("Error Occurred and Handled")


# print("end")

# def read_int(text):
#     while True:
#         try:
#             result = int(input(text))
#             return result
#         except Exception as err:
#             print(err)
#             print("enter int value ")

# a = read_int("a: ")
# print(f"{a=}")



# run = True
# while run:
#     try:
#         a = int(input("Enter your number: "))
#         if a == 0:
#             run = False
#         if a < 4:
#             b = a/(a-3) # throws ZeroDivisionError for a = 3
#         if a >= 4:
#             print("Value of b = ", b) # throws NameError
#         # note that braces () are necessary here for multiple exceptions
#     except ZeroDivisionError:
#         print("ZeroDivisionError!")
#     except NameError:
#         print("NameError!")
#     except ValueError:
#         print("ValueError")
#     except:
#         print("Error Occurred and Handled")
#     else:
#         print("Value of b = ", b)

# print("end")

# a = input("a:")
# b = input("b:")
# try:
#     a = int(a)
# except:
#     a = 0

# try:
#     b = int(b)
# except:
#     b = 0
# print(f"{a+b=} {a=} {b=}")


# def read_int(text):
#     try:
#         result = int(input(text))
#         return("try", result)
#     except Exception as err:
#         print(err)
#         print("enter int value ")
#     else:
#         return("else", result)
#     finally:
#         # return("finally", f"{result=}" )
#         print("finally", f"{result=}" )

# a = read_int("a: ")
# print(f"{a=}")




# import math
# try:
#     exp = int(input("exp:"))
#     print(math.exp(exp))
# except ValueError as err:
#     print("ValueError", err)
# except OverflowError as err:
#     print("OverflowError", err)
# except ArithmeticError as err:
#     print("ArithmeticError", type(err), err)

# e = Exception()
# a = ArithmeticError()
# z = ZeroDivisionError()
# print(isinstance(e, ArithmeticError))
# print(isinstance(a, ArithmeticError))
# print(isinstance(z, ArithmeticError))
    

# try:
#     num1, num2 = map(float, input("Enter two numbers separated by a comma: ").split(','))
    
#     result = num1 / num2
    
# except ZeroDivisionError:
#     print("Division zero is not allowed.")
    
# except ValueError:
#     print("Error: Invalid input.")
    
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
    
# else:
#     print(f" {result=}")
    
# finally:
#     print("good to use try")




def read_int(text):
    result = input(text)
    if not result.isdigit():
        raise ValueError("my error, value is not number")
    return int(result)


try:
    value = read_int("Enter a positive integer: ")
except ValueError as e:
    print(e)
else:
    print(f"{value=}")