import pygame
import random

pygame.init()
sc = pygame.display.set_mode((400, 400))
sc.fill((255, 255, 255))
pygame.display.set_caption("Lucky Game")

X, Y = 400, 400

font_large = pygame.font.SysFont('Arial', 50)
font_medium = pygame.font.SysFont('Arial', 40)
font_small = pygame.font.SysFont('Arial', 30)

# Текст на першому екрані
text1 = font_large.render('Test your luck', True, (180, 0, 0))
textRect1 = text1.get_rect(center=(X // 2, Y // 2 - 50))

text2 = font_medium.render("Press the button to start", True, (180, 0, 0))
textRect2 = text2.get_rect(center=(X // 2, Y // 2 + 10))

# Кнопка Start Game
button_surface = pygame.Surface((150, 50))
text_button = font_small.render('Start Game', True, (255, 255, 255))
buttonRect1 = text_button.get_rect(center=(75, 25))
button_rect_border = pygame.Rect(X // 2 - 75, Y // 2 + 50, 150, 50)

#Ігрові змінні
button_clicked = False
number_to_guess = random.randint(1, 100)
attempts_left = 10
user_input = ''
game_over = False
user_won = False
feedback = ""
clock = pygame.time.Clock()

def reset_game():
    global number_to_guess, attempts_left,   user_input, game_over, user_won, feedback
    number_to_guess = random.randint(1, 100)
    attempts_left = 10
    user_input = ''
    game_over = False
    user_won = False
    feedback = ""

while True:
    sc.fill((0, 0, 0))

    if not button_clicked:
        # Перший екран
        sc.blit(text1, textRect1)
        sc.blit(text2, textRect2)
        
        if button_rect_border.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface, (0, 128, 0), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (50, 55, 55), (1, 1, 148, 48))
            pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)

        button_surface.blit(text_button, buttonRect1)
        sc.blit(button_surface, button_rect_border.topleft)

    else:
        # Другий екран 
        if not game_over:
            prompt_text = font_medium.render('Enter a number (1-100):', True, (180, 0, 0))
            sc.blit(prompt_text, (20, 50))

            input_text = font_medium.render(user_input, True, (180, 0, 0))
            sc.blit(input_text, (190, 100))
            
            feedback_text = font_medium.render(feedback,True,(180,0,0))
            sc.blit(feedback_text, (150,200))

            attempts_text = font_small.render(f'Attempts left: {attempts_left}', True, (180, 0, 0))
            sc.blit(attempts_text, (110, 150))
        else:
            if user_won:
                result_text = font_large.render('You Win!', True, (0, 180, 0))
            else:
                result_text = font_large.render('You Lose!', True, (180, 0, 0))
            sc.blit(result_text, (X // 2 - result_text.get_width() // 2, Y // 2 - 25))
            restart_text = font_small.render('Press "R" to restart', True, (0, 0, 0))
            sc.blit(restart_text, (X // 2 - restart_text.get_width() // 2, Y // 2 + 50))
            number_text = font_small.render(f'The number was: {number_to_guess}', True, (180, 0, 0))
            sc.blit(number_text, (X // 2 - number_text.get_width() // 2, Y // 2 + -170))
            
            restart_text = font_small.render('Press "R" to restart', True, (180, 0, 0))
            sc.blit(restart_text, (X // 2 - restart_text.get_width() // 2, Y // 2 + 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if not button_clicked:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect_border.collidepoint(event.pos):
                    button_clicked = True
        
        elif not game_over:
            if event.type == pygame.KEYDOWN:
                if event.unicode.isdigit():
                    user_input += event.unicode
                elif event.key == pygame.K_RETURN and user_input:
                    guess = int(user_input)
                    if guess == number_to_guess:
                        user_won = True
                        game_over = True
                    else:
                        attempts_left -= 1
                        if guess < number_to_guess:
                            feedback = "Higher!"
                        else:
                            feedback = "Lower!"
                        if attempts_left == 0:
                            game_over = True
                        else:
                            user_input = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

        elif game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                reset_game()
                button_clicked = False

    pygame.display.update()
    clock.tick(30)
