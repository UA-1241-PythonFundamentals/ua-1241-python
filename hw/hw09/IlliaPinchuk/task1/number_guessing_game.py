import random

def number_guessing_game():
    while True:
        target_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10
        
        print("\nWelcome to the Number Guessing Game!")
        print("I have selected a number between 1 and 100.")
        print(f"You have {max_attempts} attempts to guess the number.\n")
        
        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            
            attempts += 1
            
            if guess < target_number:
                print("Your guess is too low.")
            elif guess > target_number:
                print("Your guess is too high.")
            else:
                print(f"Congratulations! You've guessed the number {target_number} correctly in {attempts} attempts.")
                break
            
            if attempts == max_attempts:
                print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {target_number}.")
            else:
                print(f"You have {max_attempts - attempts} attempts left.\n")
        
        while True:
            play_again = input("\nWould you like to play again? (Y/N): ").strip().lower()
            if play_again in ['y', 'n']:
                break
            else:
                print("Please enter 'Y' for Yes or 'N' for No.")
        
        if play_again == 'n':
            print("Thank you for playing! Goodbye.")
            break

number_guessing_game()
