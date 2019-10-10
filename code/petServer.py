# Following along https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
from flask import Flask
from sense_hat import SenseHat
sense = SenseHat()

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/temperature', methods=['GET'])
def get_temperature():
    return str(sense.get_temperature())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
