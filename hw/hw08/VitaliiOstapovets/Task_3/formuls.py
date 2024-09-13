from math import pi, pow

def rectangle(width, length):
    area_rectangle = width * length
    #print(f'area_rectangle = {area_rectangle}')
    return area_rectangle


def triangle(height, length):
    area_triangle = 0.5 *height*length
    #print(f'area_triangle = {area_triangle}')
    return area_triangle

def circle(radius):
    area_circle= pi*pow(radius,2)
    round_ar_cr = round(area_circle,2)
    #print(f'area_circle = {round(area_circle,2)}')
    return round_ar_cr

