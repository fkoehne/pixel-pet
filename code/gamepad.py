# Following along the lines of https://ericgoebelbecker.com/2015/06/raspberry-pi-and-gamepad-programming-part-1-reading-the-device/
from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select
from PetState import PetState
from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/

sense = SenseHat()

sense.clear(0, 0, 0)
neutral = sense.load_image("img/neutral.png")
alert = sense.load_image("img/alert.png")
eyesLeft = sense.load_image("img/EyesLeft.png")
eyesRight = sense.load_image("img/EyesRight.png")
radio = sense.load_image("img/radio.png")

state = PetState(1)
sense.set_pixels(neutral)
print (state)

gamepad = InputDevice("/dev/input/event0")
print(gamepad)

while True:
     r,w,x = select([gamepad], [], [])
     for event in gamepad.read():                
        if event.value == 1: # Press-Events (i.e. ignore release-events and arrows)                             
            print "Value " + str(event.value) + ", Type " + str(event.type) + ", Code " +str(event.code)  
            if event.code == 296: # SELECT
                sense.set_pixels(radio)              
                state = PetState.__increment__(state)
                print state
                print PetState.__int__(state)
            if event.code == 290:
                sense.set_pixels(neutral)
            if event.code == 289:
                sense.set_pixels(alert)
            if event.code == 297:
                sense.set_pixels(eyesLeft)
            if event.code == 288:
                sense.set_pixels(eyesRight)
        if event.value == 127 or event.value == 255:
            print "Value " + str(event.value) + ", Type " + str(event.type) + ", Code " +str(event.code)                              


# Event Value 1
# Blue button 288
# Red button 289
# Yellow button 290
# Green button 291

# SELECT 293
# START 297
# Left Top 292
# Right Top 293