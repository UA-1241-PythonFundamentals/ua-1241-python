import area

def calculate_area(option):
    match option:
        case 1:
            print(area.rectangle.__doc__)
            print(area.rectangle())
        case 2:
            print(area.circle.__doc__)
            print(area.circle())
        case 3:
            print(area.triangle.__doc__)
            print(area.triangle())
        case _:
            print("Invalid option!")
    

def make_choice():
    option = int(input("Which figure area do you want to calcuate (1-rectangle, 2-circle, 3-triangle): "))
    if option in range(3+1):
        calculate_area(option)
    else:
        print("Sorry! There is not such figure!")


if __name__ == "__main__":
    make_choice()