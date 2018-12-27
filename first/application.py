from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> Hello, world!</h1>"

@app.route('/andrew')
def andrew():
    return "<h1> Hello, Andrew! </h1>"

@app.route('/<name>')
def index_with_name(name):
    return "<H1> Hello, {} </h1>".format(name)