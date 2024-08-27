import pygame
import random
pygame.init()
choice =  random.randint(1, 100)
print(choice)
game_display = pygame.display.set_mode((800, 600))

your_result = ""
status= True
status_number = ""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
attempts = 10
done = False
clock = pygame.time.Clock()
point_list = []
your_number = ""
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.dict["key"] == 113:
                your_number = ""
                your_result = ""
                status= True
                status_number = ""
                attempts = 10
            if event.dict["key"] == 8 and status:
                your_number = your_number[:-1]
            if event.dict["key"] == 13 and your_number != "" and status:
                if your_number == str(choice):
                    result = True
                    your_result = "You won"
                    status = False
                else :
                     attempts -= 1
                     print(your_number)
                     if int(your_number) < choice:
                         status_number = "number is more"
                     if int(your_number) > choice:
                         status_number = "number is less"
                     your_number = ""
                     if attempts == 0:
                         your_result = "You loose"
                         status = False
                         your_number = "Hahahahaa"
                         status_number = ""
            number = event.dict["unicode"]
            if number.isdigit() and status:
                if your_number == "" or len(your_number) <= 1:
                    your_number += number
                elif your_number == "10" and number == "0":
                    your_number += number

    game_display.fill(WHITE)

    font = pygame.font.SysFont('Calibri', 60, True, False)
    font_1 = pygame.font.SysFont('Calibri', 80, True, False)
    font_2 = pygame.font.SysFont('Calibri', 30, True, False)
    text_1 = font.render("Guess the number",True, BLACK)
    text_2 = font.render("Your number:",True, BLACK)
    text_3 = font.render(your_number,True, BLACK)
    text_4 = font.render("Attempts:",True, BLACK)
    text_5 = font.render(str(attempts),True, BLACK)
    text_6 = font_1.render(your_result,True, BLACK)
    text_7 = font_2.render(status_number,True, BLACK)
    text_8 = font_2.render("rules of the game| q: new game | enter:confirm number |",True, BLACK)
    
    game_display.blit(text_1, [170, 20])
    game_display.blit(text_2, [20, 140])
    game_display.blit(text_3, [400, 145])
    game_display.blit(text_4, [20, 200])
    game_display.blit(text_5, [400, 205])
    game_display.blit(text_6, [220, 305])
    game_display.blit(text_7, [550, 185])
    game_display.blit(text_8, [40, 550])

    pygame.display.update()
    clock.tick(60)