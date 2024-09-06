#_Creating class polygon
class polygon:
    def __init__(self, user_input_width, user_input_height):
        self.width = user_input_width
        self.heigth = user_input_height
    
#_User's input
user_input_width = input("Write width of rectangle: ")
user_input_height = input("Write height of rectangle: ")
    
#_Creating class rectangle that inherits from polygon
class rectangle(polygon):
    #_Finding area of rectangle
    rectangle_area = float(user_input_width) * float(user_input_height)
    
#_Checking user's input
def check_user_input(user_input_width, user_input_height):
    if float(user_input_width) < float(user_input_height):
        #Output result
        print(f"Area of rectangle is: {round(rectangle.rectangle_area, 2)}cm2")
    elif float(user_input_width) >= float(user_input_height):
        print("Incorrect input. Width of rectangle must be less that height!")
check_user_input(user_input_width, user_input_height)
#=======================================