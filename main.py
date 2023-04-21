import pygame
import RPi.GPIO as GPIO
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
        print(d, self.last == "clear")
        if d == "clear":
            if self.last != "clear":
                sounds["clear"].play()
            self.last = "clear"
            return

        if d["vehicle"]:
            sounds["vehicle"].play()
            self.last = "vehicle"
        elif d["obstruction"]:
            sounds["obstruction"].play()
            self.last = "obstruction"
        if d["person"]:
            self.turnOn(LED)

    def turnOn(self, pin):
        GPIO.output(pin, True)

    def turnOff(self, pin):
        GPIO.output(pin, False)

    def start(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led, GPIO.OUT)

        while True:
            self.process_frame()

main = Main(True)
main.start()
