import pygame
from random import randint
pygame.init()


window = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()


font = pygame.font.SysFont(None, 50)
text = ""
input_active = True
k = False
k1 = False
b=0
m=str(randint(1,100))
i=0

answer1 = font.render("YOU WIN!",1,(0,255,0),0)
width1, height1 = answer1.get_size()

answer2 = font.render("YOU LOST!",1,(255,0,0),0)
width2, height2 = answer2.get_size()

bigger = font.render("Try a bigger number",1,(255,0,0),0)
width_big, height_big = bigger.get_size()

smaller = font.render("Try a smaller number",1,(255,0,0),0)
width_sm, height_sm = smaller.get_size()


while True:
    clock.tick(60)
    window.fill(0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN :
                if text == m:
                    k = True
                    input_active = False
                else:
                    input_active = True 
                    i+=1
                    if int(text)>int(m):
                        b=1
                    else:
                        b=2
                    text = ""
                if i>=10:
                   input_active = False 
                   k1 = True
            elif event.key == pygame.K_BACKSPACE:
                text =  text[:-1]
            else:
                text += event.unicode
        
        welcome = font.render("Guess the number from 1 to 100:",1,(255,0,255),0)
        width_wel, height_wel = welcome.get_size()
        window.blit(welcome,(300-width_wel/2,50))

        attemp = font.render("Attempts left: "+str(10-i), True, (0, 0, 255))
        width_att, height_att = attemp.get_size()
        window.blit(attemp,(300-width_att/2,100))
       
        if k:
            window.blit(answer1,(300-width1/2,400))
        if not k and b==1:
             window.blit(smaller,(300-width_sm/2,400))
        if not k and b==2:
             window.blit(bigger,(300-width_big/2,400))
        if k1:
            window.fill(0)
            window.blit(answer2,(300-width2/2,300-height2/2))

        text_surf = font.render(text, True, (255, 255, 255))
        window.blit(text_surf, text_surf.get_rect(center = window.get_rect().center))
        
        pygame.display.update()
