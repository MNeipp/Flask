from flask import Flask, render_template
from math import floor
app = Flask(__name__)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def checkerboard(x,y,color1,color2):
    return render_template("checkerboard.html", x=x, y=y, color1=color1, color2=color2)

if __name__ == "__main__":
    app.run(debug=True)