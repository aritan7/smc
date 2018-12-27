### Second Flask application - Dynamic HTMl in templates###
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # store under templates folder
    message = 'Hello world'
    return render_template("index.html", message=message)


@app.route("/<name>")
def user(name):
    message = 'Hello {}'.format(name)
    return render_template("index.html", message=message)

