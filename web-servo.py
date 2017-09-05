from flask import Flask
from flask import request
from flask import render_template
import IO

app = Flask(__name__)
myServo = IO.SERVO(12)

@app.route('/')
def index():
    return render_template("web-servo.html")

@app.route('/', methods=['POST'])
def index_post():

    if "CW" in request.form:
     myServo.CW()
    elif "CCW" in request.form:
     myServo.CCW()
    return render_template("web-servo.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

