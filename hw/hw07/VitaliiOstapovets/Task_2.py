import math
#Прямокутник
def rectangle(width, length):
    area_rectangle = width * length
    print(f'area_rectangle = {area_rectangle}')
    
#trikutnik
def triangle(height, length):
    area_triangle = 0.5 *height*length
    print(f'area_triangle = {area_triangle}')
#kolo
def circle(radius):
    area_circle= math.pi*radius**2
    print(f'area_circle = {round(area_circle,2)}')

