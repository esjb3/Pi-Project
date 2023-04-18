# load gpio and pins for cam, speaker, light
import GPIO.RPi as GPIO
GPIO.setmode(GPIO.BCM)
def setGPIO():
    gpio = [1]
    GPIO.setup(gpio, GPIO.OUT)
    
    return gpio




# function to turn on light
    # output to led pin
def turnOn(pin)
    if nothing comes turn light on
    
    GPIO.output(gpio[pin], GPIO.HIGH)
# function to play sound through speaker
    # play sound
def playSound(sound, pin):
    if something is detected sound plays
    
    
   
GPIO.cleanup()

        
