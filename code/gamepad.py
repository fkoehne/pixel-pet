# Following along the lines of https://ericgoebelbecker.com/2015/06/raspberry-pi-and-gamepad-programming-part-1-reading-the-device/
from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
from menu import PetState
from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/

sense = SenseHat()

# Each menu item is to be implemented in a separate class
sense.clear(0, 0, 0)
state = PetState(sense)

gamepad = InputDevice("/dev/input/event0")
print(gamepad)

while True:
     r,w,x = select([gamepad], [], [])
     for event in gamepad.read():                
        if event.value == 1: # Press-Events (i.e. ignore release-events and arrows)                             
            # print "Value " + str(event.value) + ", Type " + str(event.type) + ", Code " +str(event.code)  
            if event.code == 296: # SELECT                  
                state.increment()          
            else:                  
                state.signal(event.code)


# Event Value 1
# Blue button 288
# Red button 289
# Yellow button 290
# Green button 291

# SELECT 293
# START 297
# Left Top 292
# Right Top 293