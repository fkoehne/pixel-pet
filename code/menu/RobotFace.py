from BaseMenuItem import BaseMenuItem
from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/
from time import sleep


# Robot making funny eyes on the 8x8 display
class RobotFace(BaseMenuItem):
    
    def __init__(self, sense):
        self.sense = sense        
        self.neutral = sense.load_image("img/neutral.png")
        self.alert = sense.load_image("img/alert.png")
        self.eyesLeft = sense.load_image("img/EyesLeft.png")
        self.eyesRight = sense.load_image("img/EyesRight.png")  
        self.blinking = sense.load_image("img/blinking.png")     
        self.blinking_half = sense.load_image("img/blinking-half.png")     

    def select(self):
        self.doBlink()
        
    def deselect(self):
        pass

    def doBlink(self):        
        self.sense.set_pixels(self.neutral)
        sleep(0.2)
        self.sense.set_pixels(self.blinking_half)
        sleep(0.1)
        self.sense.set_pixels(self.blinking)
        sleep(0.1)
        self.sense.set_pixels(self.blinking_half)         
        sleep(0.1)
        self.sense.set_pixels(self.neutral)
        sleep(0.1)
        self.sense.set_pixels(self.blinking_half)
        sleep(0.1)
        self.sense.set_pixels(self.blinking)
        sleep(0.1)
        self.sense.set_pixels(self.neutral)       