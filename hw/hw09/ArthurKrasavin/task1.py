from random import randint
number = randint(0, 100)
attempts = 10
print("Hello, I was thinked for a number. Can u guess it?")

while attempts > 0:
    answer = int(input("\nYour answer: "))
    if answer > number:
        print("Oh, too large, try a lower number")
        attempts -=1
    if answer < number:
        print("Oh, too small, try a bigger number")
        attempts -=1
    if answer == number:
        print("\n\tCongrats!!!! You won!")
        break
else:
    print("\n\tSorry, you are out of attempts =(")