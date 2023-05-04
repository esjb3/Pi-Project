import pygame
import cv2 as cv

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

WIDTH = 810
HEIGHT = 1440

FPS = 60

pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH), pygame.RESIZABLE)

cap = cv.VideoCapture(0)

running = True
while running:
    pygame.event.get()
    _, frame = cap.read()

    screen.fill((255, 255, 255))
    surf = pygame.image.frombuffer(frame.tobytes(), frame.shape[1::-1], "BGR")
    surf = pygame.transform.scale_by(surf, (screen.get_height() * .6) / surf.get_height())
    screen.blit(surf, ((screen.get_width() - surf.get_width()) / 2 * 0.2, (screen.get_height() - surf.get_height()) / 2))
    pygame.display.flip()
