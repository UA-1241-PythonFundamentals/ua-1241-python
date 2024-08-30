def filter_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("That is a not a positive number!")
        if age % 2 == 0:
            print("Even")
        else:
            print("Odd")
    except ValueError as e:
            print(f"Error: {e}!")
            
def main():
    filter_age()
if __name__=="__main__":
    main()