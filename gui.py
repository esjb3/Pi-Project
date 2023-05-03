import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("walker.png").convert()
        self.surf = pygame.transform.scale(self.surf, (400, 600))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(200, 300))



        








                         












# collect data
# function for cars that ignore light to test efficiency of light
    # if car is detected by camera while stop light is on
        # add to counter
# function for average elapesed time that light stays on
    # while light is on start timer
    # when timer stops add the elapsed time to a list
    # every time an elapsed time is added to a list, it calculates the average
# function for amount of walkers
    # if light turns on 
        # add to counter

# GUI class
# display the data on right half of screen
# Left half will alternate pictures of a person walking (if someone is walking) or an
#  empty street (if no one is walking)
