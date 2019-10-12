# Following along https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
from flask import Flask
from gtts import gTTS
import os
from sense_hat import SenseHat
sense = SenseHat()

app = Flask(__name__)


images = [
    sense.load_image("img/neutral.png"),
    sense.load_image("img/blinking.png"),
    sense.load_image("img/EyesLeft.png"),
    sense.load_image("img/EyesRight.png"),
    sense.load_image("img/8x8face.png")
]

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/temperature', methods=['GET'])
def get_temperature():
    return str(sense.get_temperature())

@app.route('/api/say/<s>', methods=['GET'])
def say(s):
    # define variables
    tts = gTTS(s, 'de')
    file = "speech.mp3"
    tts.save(file)
    os.system("mpg123 " + file)
    return 'beep'

@app.route('/api/displayimage/<img>', methods=['GET'])
def displayimage(img):
    img = int(img)
    if img < 0:
        abort(404)
    sense.set_pixels(images[img])
    return 'done' 

displayimage(0)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
