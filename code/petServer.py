# Following along https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
from flask import Flask
from sense_hat import SenseHat
sense = SenseHat()

app = Flask(__name__)

sense.clear(0, 0, 0)
neutral = sense.load_image("img/neutral.png")
blinking = sense.load_image("img/blinking.png")
eyesLeft = sense.load_image("img/EyesLeft.png")
eyesRight = sense.load_image("img/EyesRight.png")
bright = sense.load_image("img/8x8face.png")

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/temperature', methods=['GET'])
def get_temperature():
    return str(sense.get_temperature())

@app.route('/api/displayimage/<img>', methods=['GET'])
def displayimage(img):
    if img < 0:
        abort(404)
    sense.set_pixels(neutral) # TODO get faces from a map
    return 'done' 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
