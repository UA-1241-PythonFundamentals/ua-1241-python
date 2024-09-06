def check_age():
    try:
        age = int(input("Введіть ваш вік: "))        
        if age < 0:
            raise ValueError("Вік не може бути від'ємним числом.")
        elif age % 2 == 0:
            print("Ваш вік парний.")
        else:
            print("Ваш вік непарний.")
    except ValueError as e:
        print(f"Помилка: {e}")


check_age()
#def main():
#if __name__ == "__main__":
#    main()