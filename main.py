import pygame
# import RPi.GPIO as GPIO
import time
from PIL import Image
from vision import Vision

from pygame.locals import (
    HWSURFACE,
    DOUBLEBUF,
    RESIZABLE,
    MOUSEBUTTONDOWN,
    QUIT,
)

class Main:
    def __init__(self, size, FPS):
        self.vision = Vision("yolov8n")
        self.screen = pygame.display.set_mode((size[0], size[1]), HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.clock = pygame.time.Clock()

        self.sounds = {
            0: pygame.mixer.Sound("audio/clear.mp3"),
            1: pygame.mixer.Sound("audio/caution.mp3"),
            2: pygame.mixer.Sound("audio/danger.mp3"),
        }
        self.pins = []

        self.last = (0, 0)

        self.FPS = FPS

        self.running = True

    def process(self):
        for frame in self.vision.detect():
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if self.screen.get_width() * 0.6 <= pygame.mouse.get_pos()[0] <= self.screen.get_width() * 0.6 + 220 and self.screen.get_height() * 0.55 <= pygame.mouse.get_pos()[1] <= self.screen.get_height() * 0.55 + 70:
                        self.running = True
                    if self.screen.get_width() * 0.6 + 240 <= pygame.mouse.get_pos()[0] <= self.screen.get_width() * 0.6 + 240 + 220 and self.screen.get_height() * 0.55 <= pygame.mouse.get_pos()[1] <= self.screen.get_height() * 0.55 + 70:
                        self.running = False

            self.screen.fill((120, 118, 118))

            if self.running:
                if self.vision.person:
                    # turn lights on
                    pass

                s = self.vision.status()
                if s != self.last[0] and time.time() - self.last[1] > 2:
                    self.sounds[s].play()
                    self.last = (s, time.time())

            frame = Image.fromarray(frame)

            image = pygame.image.frombuffer(frame.tobytes(), frame.size, "BGR")
            image = pygame.transform.scale_by(image, (self.screen.get_height() * 0.6) / image.get_height())
            self.screen.blit(image, ((self.screen.get_width() - image.get_width()) / 2 * 0.2, (self.screen.get_height() - image.get_height()) / 2))

            start = pygame.draw.rect(self.screen, (8, 255, 8), [self.screen.get_width() * 0.6, self.screen.get_height() * 0.55, 220, 70])
            stop = pygame.draw.rect(self.screen, (225, 6, 0), [start.right + 20, start.y, 220, 70])

            font = pygame.font.SysFont("Corbel", 35)
            start_text = font.render("Start", True, (255, 255, 255))
            stop_text = font.render("Stop", True, (255, 255, 255))

            smallerfont = pygame.font.SysFont("Corbel", 15)
            status = font.render(f"Status: {'ON' if self.running else 'OFF'}", True, (255, 255, 255))

            self.screen.blit(start_text, (start.x + 70, start.y + 18))
            self.screen.blit(stop_text, (stop.x + 76, stop.y + 18))

            pcounter = font.render(f"Pedestrians Detected: {self.vision.pcount}", True, (255, 255, 255))
            ccounter = font.render(f"Vehicles Detected: {self.vision.ccount}", True, (255, 255, 255))

            self.screen.blit(pcounter, (start.x + 10, start.y - 120))
            self.screen.blit(ccounter, (start.x + 10, start.y - 60))

            self.screen.blit(status, (start.x + 150, start.y + 80))

            pygame.display.update()
            self.clock.tick(self.FPS)

    def start(self):
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.pins, GPIO.OUT)
        self.process()

pygame.init()

main = Main((1440, 810), 60)
main.start()
