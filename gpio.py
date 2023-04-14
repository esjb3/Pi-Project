# load gpio and pins for cam, speaker, light
import GPIO.RPi as GPIO

# function to turn on light
    # output to led pin
def turnOn(light, pin):
# function to play sound through speaker
    # play sound
def playSound(sound, pin):
# function to get video feed and recursively send to vision model
def video(video, pin):
    # forever:
        # get data stream from camera output and output
        output = 
        # this could be a generator
        
