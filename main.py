import pygame
# import RPi.GPIO as GPIO
from time import sleep
from vision import Vision

pygame.init()

sounds = {
    "obstruction": pygame.mixer.Sound("caution.mp3"),
    "vehicle": pygame.mixer.Sound("stop.mp3"),
    "clear": pygame.mixer.Sound("clear.mp3"),
}

class Main(Vision):
    def __init__(self, debug=False):
        super().__init__("yolov8n", 0, debug)
        
        self.led = 13
        self.clear_count = 0
        self.debug = debug

        self.last = None

    @property
    def debug(self):
        return self._debug
    
    @debug.setter
    def debug(self, debug):
        self._debug = debug

    @property
    def last(self):
        return self._last
    
    @last.setter
    def last(self, last):
        self._last = last

    def process_frame(self):
        d = super().detect()
        if d == "clear":
            if self.last != "clear":
                sounds["clear"].play()
                self.last = "clear"
            self.clear_count += 1
            

        if d["vehicle"]:
            if self.last != "vehicle":
                sounds["vehicle"].play()
                self.last = "vehicle"
            self.clear_count = 0
        elif d["obstruction"]:
            if self.last != "obstruction":
                sounds["obstruction"].play()
                self.last = "obstruction"
            self.clear_count = 0
        elif d["person"]:
            if self.last != "clear" and self.clear_count == 10:
                sounds["clear"].play()
                self.last = "clear"
            self.clear_count += 1

        if d["person"]:
            self.turnOn(self.led)
        else:
            self.turnOff(self.led)

    def turnOn(self, pin):
        # GPIO.output(pin, True)
        self.surface.fill((255, 158, 0))
        pygame.display.flip()

    def turnOff(self, pin):
        # GPIO.output(pin, False)
        self.surface.fill((255, 255, 255))
        pygame.display.flip()

    def start(self):
        # GPIO.setmode(GPIO.BCM)
        # GPIO.setup(self.led, GPIO.OUT)
        self.surface = pygame.display.set_mode((640, 380))

        while True:
            pygame.event.get()
            self.process_frame()

main = Main(True)
main.start()
