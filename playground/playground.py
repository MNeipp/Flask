from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def boxes():
    return render_template("playground.html")

@app.route('/play/<int:num>')
def numbered_boxes(num):
    return render_template("playground.html", num=num, color="lightblue")
@app.route('/play/<int:num>/<string:color>')
def colored_boxes(num, color):
    return render_template("playground.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)