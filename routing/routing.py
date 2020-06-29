from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world!"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<string:name>')
def hello_name(name):
    return (f"Hi, {name}!")

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num,word):
    return (f"{word}" * num)

@app.errorhandler(404)
def notfound(error):
    return "Sorry, no response! Try again!"


if __name__=="__main__":
    app.run(debug=True)

