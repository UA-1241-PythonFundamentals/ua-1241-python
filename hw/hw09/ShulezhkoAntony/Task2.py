import pygame

pygame.init()

window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Rectangle Boundary Example')

rect_width = 40
rect_height = 60
rect_x = 50
rect_y = 50
rect_speed_x = 5
rect_speed_y = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    rect_x += rect_speed_x
    rect_y += rect_speed_y

    if rect_x < 0:
        rect_x = 0
        rect_speed_x = -rect_speed_x  # Reverse direction
    elif rect_x + rect_width > window_width:
        rect_x = window_width - rect_width
        rect_speed_x = -rect_speed_x  # Reverse direction

    if rect_y < 0:
        rect_y = 0
        rect_speed_y = -rect_speed_y  # Reverse direction
    elif rect_y + rect_height > window_height:
        rect_y = window_height - rect_height
        rect_speed_y = -rect_speed_y  # Reverse direction

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()
    pygame.time.Clock().tick(30)
