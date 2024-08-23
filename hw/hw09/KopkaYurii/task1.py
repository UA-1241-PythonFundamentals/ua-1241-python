import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    
    attempts = 10
    
    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("You have 10 attempts to guess it. Good luck!\n")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            
            if guess == number_to_guess:
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempt} attempts!")
                break
            elif guess < number_to_guess:
                print("Too low! Try again.\n")
            else:
                print("Too high! Try again.\n")
        
        except ValueError:
            print("Please enter a valid number.\n")
            continue
        
        if attempt == attempts:
            print(f"Sorry, you've used all {attempts} attempts. The number was {number_to_guess}. Better luck next time!")

guessing_game()