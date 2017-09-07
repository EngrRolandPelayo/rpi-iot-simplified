from flask import Flask
from flask import request
from flask import render_template
import IO

app = Flask(__name__)
myLED = IO.LED(7)
status = "Off"

@app.route('/')
def index():
    myLED.OFF()
    return render_template("web-switch.html")

@app.route('/', methods=['POST'])
def index_post():
    global status
    if "On" in request.form: 
     turnONLED()
     status = "On"
    elif "Off" in request.form:
     turnOFFLED()
     status = "Off"
    return render_template("web-switch.html", value=status)

def turnONLED():
  myLED.ON()

def turnOFFLED():
  myLED.OFF()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

