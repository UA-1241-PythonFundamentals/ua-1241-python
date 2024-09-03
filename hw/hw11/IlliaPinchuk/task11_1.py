def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return f"The age {age} is {'even' if age % 2 == 0 else 'odd'}."

def main():
    try:
        age = int(input("Enter your age: "))
        result = process_age(age)
        print(result)
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
