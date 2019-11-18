import schedule
import time
import random
from sense_hat import SenseHat

sense = SenseHat()

images = [
    sense.load_image("../img/neutral.png"),        # 0
    sense.load_image("../img/blinking.png"),       # 1
    sense.load_image("../img/blinking-half.png"),  # 2
    sense.load_image("../img/EyesLeft.png"),       # 3
    sense.load_image("../img/EyesRight.png"),      # 4 
    sense.load_image("../img/alert.png")           # 5
]

def displayRandomImage():
    img = int(random.randint(0,5))
    sense.set_pixels(images[img])
    return 'done' 

schedule.every(2).seconds.do(displayRandomImage)

while True:
    schedule.run_pending()
    time.sleep(1)