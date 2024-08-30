# list
# inst = list()


# class Point:
#     """class Point
#     """
#     pass

# p = Point()
# print(type(p), p)


# class Point:
#     """class Point
#     """
#     count = 0

#     def print(self):
#         print(self)
#         print(self.count)


# p1 = Point()
# p2 = Point()
# print(type(p1), p1)
# print(type(p2), p2)
# print(p1.count)
# print(p2.count)
# p1.count = 20
# p1.print()
# p2.print()
# print(Point.count)
# print(Point.print)
# print(Point.__doc__)

# f = Point.print

# # f() #TypeError: Point.print() missing 1 required positional argument: 'self'
# f([15])

# def my_print(a, b):
#     print(f"{a=} {b=}")

# my_print(15, 25)
# # p1.my_print(15, 15) #AttributeError: 'Point' object has no attribute 'my_print'
# Point.g = my_print

# p1.g(15)


# class A:
#     a = 0
#     def __init__(self, b=0) -> None:
#         self.b = b

#     def print(self):
#         print(f"{self.a} {self.b}")

# a1 = A()
# a2 = A(15)
# a1.print()
# a2.print()

# a1.b = 20
# A.a = 30

# a1.print()
# a2.print()

# print(dir(a1))
# print(a1.__dict__)
# print(a2.__dict__)
# print(A.__dict__)


class Point:
    def __init__(self, x=0, y=0):
        print(f"create Point {x} {y}")
        self.__x = x
        self.__y = y

    def get_x(self):
        print("get", self)
        return self.__x
    def set_x(self, x):
        print("set", self, x)
        self.__x = x

    x = property(get_x, set_x)


    @property
    def y(self):
        print("get", self)
        return self.__y
    @y.setter
    def y(self, y):
        print("set", self, y)
        self.__y = y

    # def __del__(self):
    #     print(f"delete Point {id(self)=}, {self}")
    def __str__(self) -> str:
        return f"<x={self.__x} y={self.__y}>"

    def __repr__(self) -> str:
        return f"({self.__x}, {self.__y})"

    def distance_to_zero(self):
        return (self.__x**2 + self.__y**2) ** 0.5

    def distance(self, point):
        return ((self.__x - point.__x) ** 2 + (self.__y - point.__y) ** 2) ** 0.5

    def __lt__(self, other):
        return self.distance_to_zero() < other.distance_to_zero()

    def __add__(self, other):
        point = Point()
        point.x = self.__x + other.__x
        point.y = self.__x + other.__y
        return point


# p1 = Point(1, 1)
# p2 = Point(3, 5)
# print(p1, p2)
# print([p1, p2])
# print(p1.distance_to_zero())
# print(p2.distance_to_zero())
# print(p2.distance(p1))


# # def distance(point_1, point_2):
# #     return ((point_1._Point__x - point_2._Point__x) ** 2 + (point_1._Point__y - point_2._Point__y) ** 2) ** 0.5



# print(distance(p2, p1))

# from random import randint

# points = [Point(randint(0, 10), randint(0, 10)) for _ in range(10)]
# print(points)

# print(points[0] < points[1])
# points.sort()
# print(points)

# p = points[-1] + points[-2]
# print(p)


class Point3D(Point):
    def __init__(self, x=0, y=0, z=0):
        print("create Point3D")
        super().__init__(x, y)
        self.z = z
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"


print("Point3D".center(20))
pd1 = Point3D(99, 88, 999)

# print(dir(pd1))
print(pd1)
print([pd1])

# p3 = Point(99, 88)
# print(p3.x)
# p3.x = 999
# print(p3)

# print(p3.y)
# p3.y = 888
# print(p3)