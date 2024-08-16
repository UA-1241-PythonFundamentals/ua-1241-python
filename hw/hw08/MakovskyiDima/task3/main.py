from get_area import get_area_circle, get_area_rectamgle, get_area_triangle

def get_area_figure():
    match input("write name figure: circle, rectamgle or triangle: "):
        case "circle":
            return get_area_circle(float(input("write radius: ")))
        
        case "triangle":
            return get_area_triangle(float(input("write the height of the triangle: ")), float(input("write the side on which the height falls: ")))
        
        case "rectamgle":
            return get_area_triangle(float(input("write first side: ")), float(input("write second side: ")))
        
        case _ :
            return "wrong name figure"


if __name__ == "__main__":
    print(get_area_figure())