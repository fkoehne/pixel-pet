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
        self.radioProcess = subprocess.Popen("cvlc https://wdr-diemaus-live.icecastssl.wdr.de/wdr/diemaus/live/mp3/128/stream.mp3", shell=True, stderr=subprocess.STDOUT)    

    def deselect(self):
        self.radioProcess.terminate()
        subprocess.Popen("killall vlc", shell=True, stderr=subprocess.STDOUT)
        
    def loop(self):
        pass

    # Let the radio react to gamepad activity
    def signal(self, code):
        print str(self.__class__) + " received Code " + str(code)
        self.playLocal()
        self.deselect()
        if code == 291: # Green button             
            self.radioProcess = subprocess.Popen("cvlc https://wdr-diemaus-live.icecastssl.wdr.de/wdr/diemaus/live/mp3/128/stream.mp3", shell=True, stderr=subprocess.STDOUT)        
        if code == 289: # Red button             
            self.radioProcess = subprocess.Popen("cvlc http://209.63.239.148:8000", shell=True, stderr=subprocess.STDOUT)        
        if code == 290: # Yellow button
            self.radioProcess = subprocess.Popen("cvlc http://69.30.243.166:10034/", shell=True, stderr=subprocess.STDOUT)
        if code == 288: # Blue button
            self.radioProcess = subprocess.Popen("cvlc http://51.255.235.165:5068/stream ", shell=True, stderr=subprocess.STDOUT)
                           

    def playLocal(self):
        subprocess.Popen("mpg123 " + "sounds/397253__screamstudio__robot_part1.mp3", shell=True, stderr=subprocess.STDOUT)       
        return 'beep'
       