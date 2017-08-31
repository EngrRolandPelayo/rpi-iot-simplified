from flask import Flask
from flask import request
from flask import render_template
import LiquidCrystalPi as LCD
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

app = Flask(__name__)
LCD = LCD.LCD(29, 31, 33, 35, 37, 38)
LCD.begin(16, 2)

@app.route('/')
def my_form():
    return render_template("web-to-lcd.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text = text.upper()
    LCD.clear()
    LCD.write(processed_text)
    return processed_text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
