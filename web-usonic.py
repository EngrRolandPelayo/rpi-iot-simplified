from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import IO
import datetime

app = Flask(__name__)
myUSONIC = IO.USONIC(11,13)

@app.route('/')
def index():
    return render_template("web-usonic.html")

@app.route('/get-distance')
def get_distance():
    distance = datetime.datetime.now().time().strftime("%-S") #distance = myUSONIC.GETDISTANCE()
    #print distance 
    return distance +" cm"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

