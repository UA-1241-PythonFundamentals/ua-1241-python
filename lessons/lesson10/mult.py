# class X:
#     def p(self):
#         print("X")
# class Y:
#     def p(self):
#         print("Y")
# class Z:
#     def p(self):
#         print("Z")
# class A(X, Y):pass
# class B(Z, Y):pass
# class M(A, B, Z):pass

# m = M()
# m.p()
# print(M.__mro__)


# class Test:
#     def f1(self):
#         print(f"self:{id(self)}")

#     @classmethod
#     def f2(cls):
#         print(f"cls:{id(cls)}")

#     @staticmethod
#     def f3():
#         print(f"static")

# t1 = Test()
# t2 = Test()
# print(f"Test\t{id(Test)}")
# print(f"t1\t{id(t1)}")
# print(f"t2\t{id(t2)}")

# # Test.f1() #TypeError: Test.f1() missing 1 required positional argument: 'self'
# t1.f1()
# t2.f1()

# Test.f2()
# t1.f2()
# t2.f2()

# Test.f3()
# t1.f3()
# t2.f3()


class Encapsulation:
    def __init__(self, a, b, c):
        self.public = a
        self._protected = b
        self.__private = c

    def __str__(self):
        return f"""
            {self.public}
            {self._protected} 
            {self.__private}"""

e = Encapsulation(1,2,3)

print(e)
print(e.public)
print(e._protected)
# print(e.__private)#AttributeError: 'Encapsulation' object has no attribute '__private'
print(e._Encapsulation__private)