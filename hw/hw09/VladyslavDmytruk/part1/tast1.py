import random

def guess_number_game():
    secret_number = random.randint(1, 100)
    attempts = 10

    print("Welcome to the Number Guessing Game!")
    print("You need to selected a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

if __name__ == "__main__":
    guess_number_game()
