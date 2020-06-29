from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    employees =[
        {'first_name':'Mason', 'last_name':'Neipp'},
        {'first_name':'Monty', 'last_name':'Preston'},
        {'first_name':'Sarah', 'last_name':'Maxwell'},
        {'first_name':'Margot', 'last_name':'Reybitz'},
    ]
    return render_template("index.html", employees=employees)

if __name__ == "__main__":
    app.run(debug=True)