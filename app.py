from flask import Flask, request, render_template
import time
from checkRoom import *
app = Flask(__name__)






name = "PDS Tour App"
rooms = [100, 101, 102, 103, 104, 105, 225, 226, 227]


@app.route('/', methods=["GET", "POST"])
def pfp():
    return render_template('main.html')


@app.route('/result', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        room = request.form.get("fname")
        # getting input with name = lname in HTML form
        try:
            checkRoom(room)
            return render_template('result.html', fname=room)
        except:

            time.sleep(2)
            return render_template('main.html')


@app.route('/tour')
def fgf():
    return render_template('tour.html')




if __name__ == '__main__':
    app.run()

