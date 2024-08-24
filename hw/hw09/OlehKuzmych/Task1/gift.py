import pygame
import os

__all__ = ["showCardWinner", "showCardLosser"]

def showCardWinner():
    createCard("win.jpg")

def showCardLosser():
    createCard("lose.jpg")

def createCard(image):

    pygame.init()
    SIZE = (600,400)
    winDisplay = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Game over")

    current_directory = os.path.dirname(__file__)
    path_to_image = os.path.join(current_directory, "images", image)
    card_location = pygame.image.load(path_to_image)

    #clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        winDisplay.blit( pygame.transform.scale(card_location, SIZE), [0, 0] )
        pygame.display.update()
        #clock.tick(60)


if __name__ == "__main__":
    print("You need to call guess_num.py")

