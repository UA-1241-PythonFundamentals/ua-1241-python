import pygame 
from random import randint

pygame.init()
GameDisplay = pygame.display.set_mode((800, 600))
HEADING = pygame.font.Font(None, 24)
REGULAR_TEXT = pygame.font.Font(None, 20)

number = randint(1, 100)
attempts = 10
guess = ""
message = "Guess the number between 1 and 100 in 10 attempts"

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True
welcome = True

while running:
    GameDisplay.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if welcome:
                welcome = False
            elif event.key == pygame.K_RETURN:
                if guess.isdigit() and attempts > 0:
                    guess_num = int(guess)
                    if guess_num == number:
                        message = "Congratulations! You guessed the number!"
                        attempts = 0
                    elif guess_num < number:
                        message = "Your number is too low :("
                        attempts -= 1
                    else:
                        message = "Your number is too big :("
                        attempts -= 1
                
                    guess = ""
            elif event.key == pygame.K_BACKSPACE:
                guess = guess[:-1]
            else:
                if event.unicode.isdigit():
                    guess += event.unicode
            
    if welcome:
        greeting = HEADING.render("Hello :) Press any key to start the game", True, BLACK)
        GameDisplay.blit(greeting, (400 - greeting.get_width(), 300 - greeting.get_height()))
    else: 
        if attempts <= 0 and guess_num != number:
            end = HEADING.render(f"You didn`t guess the number :( Chosen number was {number}", True, BLACK)
            GameDisplay.blit(end, (400 - greeting.get_width(), 300 - greeting.get_height()))
        
        display_messages = REGULAR_TEXT.render(message, True, BLACK)
        GameDisplay.blit(display_messages, (50, 50))

        attempts_text = REGULAR_TEXT.render(f"Attempts left: {attempts}", True, BLACK)
        GameDisplay.blit(attempts_text, (50, 100))
        
        guess_text = REGULAR_TEXT.render(f"Your guess: {guess}", True, BLACK)
        GameDisplay.blit(guess_text, (50, 150))

    pygame.display.flip()

pygame.quit()
