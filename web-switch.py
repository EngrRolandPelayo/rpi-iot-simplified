from flask import Flask
from flask import request
from flask import render_template
import IO

app = Flask(__name__)
myLED = IO.LED(7)

@app.route('/')
def index():
    return render_template("web-switch.html")

@app.route('/', methods=['POST'])
def index_post():

    if "On" in request.form: 
     turnONLED()
    elif "Off" in request.form:
     turnOFFLED()
    return render_template("web-switch.html")

def turnONLED():
  myLED.ON()

def turnOFFLED():
  myLED.OFF()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

