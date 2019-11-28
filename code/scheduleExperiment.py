import schedule
import time
import random
from menu import RobotFace
from sense_hat import SenseHat

sense = SenseHat()
face = RobotFace(sense)

def displayRandomImage():
    face.doBlink()
    print "Blink"
    return 'done' 

schedule.every(5).seconds.do(displayRandomImage)

while True:
    schedule.run_pending()
    time.sleep(1)