# Following along the lines of https://ericgoebelbecker.com/2015/06/raspberry-pi-and-gamepad-programming-part-1-reading-the-device/
from evdev import InputDevice, categorize, ecodes, KeyEvent
from select import select

from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/

sense = SenseHat()

sense.clear(0, 0, 0)
neutral = sense.load_image("img/neutral.png")
alert = sense.load_image("img/alert.png")
eyesLeft = sense.load_image("img/EyesLeft.png")
eyesRight = sense.load_image("img/EyesRight.png")


sense.set_pixels(neutral)


gamepad = InputDevice("/dev/input/event0")
print(gamepad)
while True:
     r,w,x = select([gamepad], [], [])
     for event in gamepad.read():        
        if event.value == 1: # Press-Events (i.e. ignore release-events)
            print (str(event.type) + " " +str(event.code))                   
            if event.code == 290:
                sense.set_pixels(neutral)
            if event.code == 289:
                sense.set_pixels(alert)
            if event.code == 297:
                sense.set_pixels(eyesLeft)
            if event.code == 296:
                sense.set_pixels(eyesRight)

