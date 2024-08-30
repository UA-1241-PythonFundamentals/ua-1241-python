import random
def game():
    r_namber = random.randint(1,100)
    runs=10
    print("Welcome to the guessing game!\nI have chosen a number between 1 and 100.\nYou have 10 attempts to guess it.")
    for i in range(runs):
        guess = int(input(f"Attempt {i+1}: Enter your guess: "))
        if guess < r_namber:
            print("Too low! Try again.")
        elif guess >r_namber:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            break
    else:
          print(f"Sorry, you've used all your attempts. The number was {r_namber}.")

game()