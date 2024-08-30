import random

def guess_the_number():
    game = "Number Guessing"
    number_to_guess = random.randint(1, 100)
    attempts = 10

    print(f"Welcome to the {game} Game!")
    print("I have randomly selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it. Good luck!\n")

    for attempt in range(1, attempts + 1):
        user_guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if user_guess < number_to_guess:
            print("Too low! Try again.\n")
        elif user_guess > number_to_guess:
            print("Too high! Try again.\n")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempt} attempts!")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

guess_the_number()
