from BaseMenuItem import BaseMenuItem
from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/
import subprocess
from pathlib import Path
import random

# A simple music player
class MusicPlayer(BaseMenuItem):
    
    def __init__(self, sense):
        self.sense = sense
        self.image = sense.load_image("img/walker/Volcano.png")        

    def select(self):
        self.sense.set_pixels(self.image)         
        mp3s = list(Path('/home/pi/Music').rglob('*.mp3')) 
        print("Found the following music files...")
        for mp3 in mp3s:
            print(mp3)
        print("Playing random file...")        
        cmd = "mpg123 -v '" + str(random.choice(mp3s)) + "'"
        print (cmd)
        self.playerProcess = subprocess.Popen(cmd, shell=True, stderr=subprocess.STDOUT)      

    def deselect(self):
        self.playerProcess.terminate()
        subprocess.Popen("killall mpg123", shell=True, stderr=subprocess.STDOUT)
        
    def loop(self):        
        pass

    # Let the radio react to gamepad activity
    def signal(self, code):
        print str(self.__class__) + " received Code " + str(code)
        pass