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
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(400, 300))

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
        pygame.display.update()

    screen.fill((255, 255, 255))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()
        








                         












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
