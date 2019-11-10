# Following along the lines of https://ericgoebelbecker.com/2015/06/raspberry-pi-and-gamepad-programming-part-1-reading-the-device/
from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
from menu import PetState
from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/
import time

sense = SenseHat()

# Each menu item is to be implemented in a separate class
sense.clear(0, 0, 0)
state = PetState(sense)

gamepad = InputDevice("/dev/input/event0")
print(gamepad)

# After a while, the pet robot will go to sleep
# if there is no interaction
now = time.monotonic()
futureSleepTime = now + 1 * 30 * 60 # Half an hour sleep timer

while True:
     time.sleep(0.1)
     # Sleep if nothing happend during the last sleep time
     if time.monotonic() < futureSleepTime:    
         state.sleep()

     r,w,x = select([gamepad], [], [])
     for event in gamepad.read():                
        if event.value == 1: # Press-Events (i.e. ignore release-events and arrows)                             
            futureSleepTime = now + 1 * 30 * 60 # Half an hour, again
            # print "Value " + str(event.value) + ", Type " + str(event.type) + ", Code " +str(event.code)  
            if event.code == 296: # SELECT                  
                state.increment()          
            else:                  
                state.signal(event.code)        