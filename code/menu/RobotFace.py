from BaseMenuItem import BaseMenuItem
from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/
from time import sleep
import random

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
        self.walker = [sense.load_image("img/walker/1.png"),
                       sense.load_image("img/walker/2.png"),
                       sense.load_image("img/walker/3.png"),
                       sense.load_image("img/walker/4.png"), 
                       sense.load_image("img/walker/5.png")]
        self.treasures = [sense.load_image("img/walker/Flower.png"),
                          sense.load_image("img/walker/Flower2.png"),
                          sense.load_image("img/walker/Flower3.png")]               

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

    # Let the face react to gamepad activity
    def signal(self, code):
        print str(self.__class__) + " received Code " + str(code)
        if code == 291: # Green button 
            self.sense.set_pixels(self.eyesLeft) 
        if code == 289: # Red button
            self.sense.set_pixels(self.eyesRight) 
        if code == 290: # Yellow button
            self.doBlink()
        if code == 288: # Blue button
            self.sense.set_pixels(self.alert)
        if code == 292: # top left
            pass
        if code == 293: # top right, walk around and then find a random treasure
            for x in range(1, random.randint(2,5)):
                self.doWalker()
            self.sense.set_pixels(self.treasures[random.randint(0,len(self.treasures)-1)])
            sleep(3)
            self.sense.set_pixels(self.neutral)

    def doWalker(self):
        for x in range(0, len(self.walker)):
            self.sense.set_pixels(self.walker[x])
            print x
            sleep(0.2)
        