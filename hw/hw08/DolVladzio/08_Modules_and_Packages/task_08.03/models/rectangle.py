def rectangleArea():
    #_User's data
    rectangle_width = input("- Write width of rectangle: ") 
    rectangle_lendth = input("- Write lendth of rectangle: ") 
    #_Checking correct data
    #_1_Showing some mistakes(if it'll be:))
    if float(rectangle_width) <= 0 and float(rectangle_lendth) <= 0:
        print(f"- You have some mistakes:\n- Width of rectangle can't be {rectangle_width} only > 0\n- Lendth of rectangle can't be {rectangle_lendth}, only > 0, but < width")
    #_2_Showing result(If all will be alright:))
    elif float(rectangle_lendth) < float(rectangle_width):
        rectangle_area = float(rectangle_lendth) * float(rectangle_width)
        print(f"- Area of rectangle: {rectangle_area}cm2")
    #_3_Showing another some mistakes(if it'll be:))      
    else:
        print(f"- Lendth of rectangle can't be {rectangle_lendth}, only < rectangle of width")