def main():
    age_input = input("Plese input your age:")
    check_age(age_input)
def check_age(number):
    try:
        if number[0]  == "-":
            raise ValueError
        age = int(number)
        if age <= 0:
            raise ValueError
        elif age %2 == 0:
            print("Your age is even!")
        elif age %2 == 1:
            print("Your age is odd!")
    except ValueError as e:
        print("Incorect age")
    except Exception as er:
        er("Hi hihihih")
    

if __name__ == "__main__":
    main()