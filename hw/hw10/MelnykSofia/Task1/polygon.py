class Polygon:

    """Class Polygon finds the square of the polygon"""

    def __init__(self, num_sides):
        """ Створюємо метод конструктор"""
        self.num_sides = num_sides #створюється змінна num_sides, яка вказує на кількість сторін
        self.sides = [0 for i in range(num_sides)] #створюється ліст зі довжин сторін
    
    def inputSides(self):
        """ Створюємо метод для введення довжин сторін багатокутника"""
        self.sides =[float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def displaySides(self):
        """ Створюємо метод, який виводить на дисплеї сторону та її довжину"""
        for i in range(self.num_sides):
            print("Side",i+1,"is",self.sides[i])    