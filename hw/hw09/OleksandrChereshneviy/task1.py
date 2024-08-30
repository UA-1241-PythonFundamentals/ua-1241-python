import pygame 
import sys
import random


pygame.init() 

clock = pygame.time.Clock() 

# it will display on screen 
screen = pygame.display.set_mode([600, 500]) 

attempt = 0
result = False
rand = random.randint(0,100)
# basic font for user typed 
base_font = pygame.font.Font(None, 32) 
user_text = ''
text_result = 'You dont try to guess'
font = pygame.font.SysFont('Calibri', 25, True, False)
text_enter = font.render("Input number and press Enter: ",True,(0,0,0))

def check_res(result, attempt, rand, choise):
	if result == False and attempt == 9:
		return "Sorry yours attempt limit is over. You loose"
	elif result == False and attempt < 10:
		if rand > choise:
			return "Random number is bigger when yours"
		else:
			return "Random number is smallest when yours"
	else:
		return "YOU WIN"

# create rectangle 
input_rect = pygame.Rect(10, 100, 40, 32) 

# color_passive = pygame.Color('chartreuse4') 
color = pygame.Color('chartreuse4') 

while True: 
	for event in pygame.event.get(): 

	# if user types QUIT then the screen will close 
		if event.type == pygame.QUIT: 
			pygame.quit() 
			sys.exit() 

		if event.type == pygame.KEYDOWN:
			# Check for backspace 
			if event.key == pygame.K_BACKSPACE: 
				# get text input from 0 to -1 i.e. end. 
				user_text = user_text[:-1]
			elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
				if len(user_text) > 0 and attempt < 10 and result == False:
					if int(user_text) == rand:
						result = True
					text_result = check_res(result,attempt,rand,int(user_text))
					attempt += 1
					user_text = ""
			elif len(user_text) <= 1 and ord(event.unicode) >= 48 and ord(event.unicode) <= 57:
					user_text += event.unicode
	
	# it will set background color of screen 
	screen.fill((255, 255, 255)) 

	pygame.draw.rect(screen, color, input_rect, 2) 

	text_surface = base_font.render(user_text, True, (0, 0, 0)) 
	text_attempt = font.render(f"Attempt: {attempt}",True,(0,0,0))
	text_res = font.render(text_result,True,(0,0,0))
	
	# render at position stated in arguments 
	screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
	screen.blit(text_enter, (input_rect.x, input_rect.y-40))
	screen.blit(text_attempt, (input_rect.x, input_rect.y+40))
	screen.blit(text_res, (input_rect.x, input_rect.y+80))
	
	input_rect.w = max(100, text_surface.get_width()+10) 
	
	pygame.display.flip() 
	
	clock.tick(60) 
