from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/

class Radio():
    
    def __init__(self, sense):
        self.sense = sense
        self.image = sense.load_image("img/radio.png")        

    def select(self):
        self.sense.set_pixels(self.image) 
        # cvlc http://wdr-kiraka-live.icecast.wdr.de/wdr/kiraka/live/mp3/128/stream.mp3 

    def deselect(self):
        self.sense.set_pixels(self.image) 
        # Stop streaming