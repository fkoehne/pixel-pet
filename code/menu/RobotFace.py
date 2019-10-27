from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/

# Robot making funny eyes on the 8x8 display
class RobotFace():
    
    def __init__(self, sense):
        self.sense = sense        
        self.neutral = sense.load_image("img/neutral.png")
        self.alert = sense.load_image("img/alert.png")
        self.eyesLeft = sense.load_image("img/EyesLeft.png")
        self.eyesRight = sense.load_image("img/EyesRight.png")       

    def select(self):
        self.sense.set_pixels(self.neutral) 
        
    def deselect(self):
        pass        