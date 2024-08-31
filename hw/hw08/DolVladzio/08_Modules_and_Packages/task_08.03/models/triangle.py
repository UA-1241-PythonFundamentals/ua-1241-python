def triangleArea():
    #_User's data
    triangle_base = input("Write a base of triangle: ")
    triangle_height = input("Write a height of triangle: ")
    #_Checking correct data
    #_1_Showing some mistakes(if it'll be:))
    if float(triangle_base) <= 0 and float(triangle_height) <= 0:
        print(f"- You have some mistakes:\n- Base of triangle can't be {triangle_base} only > 0\n- Hiegth of triangle can't be {triangle_height}, only > 0 but < base")
    #_2_Showing result(If all will be alright:))
    elif float(triangle_height) < float(triangle_base):
        triangle_area = (1/2) * float(triangle_base) * float(triangle_height)
        print(f"- Area of triangle: {triangle_area}cm2")
    #_3_Showing another some mistakes(if it'll be:))         
    else:
        print(f"- Hieght of triangle can't be {triangle_height}, only < base")