import random

def guess_number_game():
    print("Welcome to 'Guess a Number' game!")
    print("I will generate a number from 1 to 100, try to guess it :)")

    rand_n = random.randint(1, 100)
    attempts = 10

    for i in range(attempts):
        user_input = input(f"Attempt #{i + 1}: What is your guess (1-100): ")
        
        if not user_input.isdigit():
            print("Error. We accept only digits from 1 to 100. Please try again.")
            continue
        
        user_n = int(user_input)
        
        if user_n < 1 or user_n > 100:
            print("Oops, your number is not in the range from 1 to 100. Please try again.")
            continue
        
        if user_n > rand_n:
            print(f"Oops, your number {user_n} is greater than the generated number. Please try again.")
        elif user_n < rand_n:
            print(f"Oops, your number {user_n} is less than the generated number. Please try again.")
        else:
            print(f"Congratulations! You guessed the number {rand_n} correctly!")
            break
    else:
        print(f"Sorry, you've used all {attempts} attempts. The generated number was {rand_n}.")

# Run the game
guess_number_game()
