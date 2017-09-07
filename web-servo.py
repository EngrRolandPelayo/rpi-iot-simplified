from flask import Flask
from flask import request
from flask import render_template
import IO

app = Flask(__name__)
myServo = IO.SERVO(12)

@app.route('/')
def index():
    #myServo.CCW()
    return render_template("web-servo.html")

@app.route('/', methods=['POST'])
def index_post():
    pos = None
    if "CW" in request.form:
     myServo.CW()
     pos = "CW"
    elif "CCW" in request.form:
     myServo.CCW()
     pos = "CCW"
    return render_template("web-servo.html", value = pos)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

