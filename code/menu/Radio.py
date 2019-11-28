from BaseMenuItem import BaseMenuItem
from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/
import subprocess

# A simple streaming radio
class Radio(BaseMenuItem):
    
    def __init__(self, sense):
        self.sense = sense
        self.image = sense.load_image("img/radio.png")        

    def select(self):
        self.sense.set_pixels(self.image) 
        self.playLocal()
        self.radioProcess = subprocess.Popen("cvlc http://wdr-kiraka-live.icecast.wdr.de/wdr/kiraka/live/mp3/128/stream.mp3", shell=True, stderr=subprocess.STDOUT)    

    def deselect(self):
        self.radioProcess.terminate()
        subprocess.Popen("killall vlc", shell=True, stderr=subprocess.STDOUT)
        
    def loop(self):
        pass

    # Let the radio react to gamepad activity
    def signal(self, code):
        print str(self.__class__) + " received Code " + str(code)
        self.deselect()
        if code == 291: # Green button             
            self.playLocal()

    def playLocal(self):
        subprocess.Popen("mpg123 " + "sounds/397253__screamstudio__robot_part1.mp3", shell=True, stderr=subprocess.STDOUT)       
        return 'beep'
       