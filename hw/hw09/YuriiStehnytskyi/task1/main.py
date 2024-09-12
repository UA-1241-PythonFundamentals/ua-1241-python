import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the guessing game!")
    print("I have chosen a number between 1 and 100. You have 10 attempts to guess it!")

    while attempts < 10:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")
                return

        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Sorry, you've used all 10 attempts. The number was {number_to_guess}.")

guessing_game()
