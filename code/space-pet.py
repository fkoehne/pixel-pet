from sense_hat import SenseHat # https://pythonhosted.org/sense-hat/api/
from time import sleep

sense = SenseHat()

sense.clear(0, 0, 0)
neutral = sense.load_image("img/neutral.png")
blinking = sense.load_image("img/blinking.png")
eyesLeft = sense.load_image("img/EyesLeft.png")
eyesRight = sense.load_image("img/EyesRight.png")
bright = sense.load_image("img/8x8face.png")


sense.set_pixels(neutral)
def animate():        
        sense.set_pixels(neutral)
        sleep(2)
        sense.set_pixels(blinking)
        sleep(0.4)
        sense.set_pixels(neutral)
        sleep(2.3)
        sense.set_pixels(eyesLeft)
        sleep(1.5)
        sense.set_pixels(blinking)
        sleep(0.3)
        sense.set_pixels(eyesRight)
        sleep(2)

h2 = 0        
def reactToMovement():  
        x, y, z = sense.get_accelerometer_raw().values()
        #h = sense.get_humidity()       
        #print(h)
        if x>-0.5 and x <0.5:
                sense.set_pixels(neutral)
        if x<=-0.5: 
                sense.set_pixels(eyesLeft)
        if x>=0.5: 
                sense.set_pixels(eyesRight)
        sleep(0.1)

while True:
    animate()
    reactToMovement()