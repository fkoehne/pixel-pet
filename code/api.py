# Following along https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
import subprocess
import os
from flask import Flask
from gtts import gTTS
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()

images = [
    sense.load_image("img/neutral.png"),        # 0
    sense.load_image("img/blinking.png"),       # 1
    sense.load_image("img/blinking-half.png"),  # 2
    sense.load_image("img/EyesLeft.png"),       # 3
    sense.load_image("img/EyesRight.png"),      # 4 
    sense.load_image("img/alert.png")           # 5
]

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/temperature', methods=['GET'])
def get_temperature():
    return str(sense.get_temperature())

@app.route('/api/say/<s>', methods=['GET'])
def say(s):
    # Getting the speech synthesis takes a moment, hence we play a prepared sound asap and async 
    # to make the system appear more responsive and get some attention.
    subprocess.Popen("mpg123 " + "sounds/397253__screamstudio__robot_part1.mp3", shell=True, stderr=subprocess.STDOUT)
    # Then we encode and use the text originally provided
    tts = gTTS(s, 'de')
    file = "speech.mp3"
    tts.save(file)
    subprocess.Popen("mpg123 " + file, shell=True, stderr=subprocess.STDOUT)
    return 'beep'

@app.route('/api/displayimage/<img>', methods=['GET'])
def displayimage(img):
    img = int(img)
    sense.set_pixels(images[img])
    return 'done' 

@app.route('/api/blink', methods=['GET'])
def blink():
    doBlink()
    return 'done' 

# Initial blinking on startup
def doBlink():        
        sense.set_pixels(images[1])
        sleep(0.2)
        sense.set_pixels(images[2])
        sleep(0.1)
        sense.set_pixels(images[5])
        sleep(0.1)
        sense.set_pixels(images[0])         
        sleep(0.1)
        sense.set_pixels(images[2])
        sleep(0.1)
        sense.set_pixels(images[1])
        sleep(0.1)
        sense.set_pixels(images[2])
        sleep(0.1)
        sense.set_pixels(images[0])         

# Make some noise
subprocess.Popen("mpg123 " + "sounds/397253__screamstudio__robot_part1.mp3", shell=True, stderr=subprocess.STDOUT)
doBlink()        

# Run the server and wait for http commands
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
