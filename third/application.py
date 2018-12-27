### Third Flask application - Request, control statement (if, for) in templates ###
from flask import Flask, render_template, redirect, url_for
from flask import request

app = Flask(__name__)
login_status = False
user = ""


@app.route('/')
def index():
    # store under templates folder
    return render_template("index.html", login_status=login_status, user=user )


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username']:
            login_status = True
            user = request.form['username']
            return render_template('index.html', login_status=login_status, user=user)
        else:
            login_status = False
            error = 'Invalid username'
            return render_template('index.html', error=error)
    else:
        return redirect(url_for('index'))


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    login_status = False
    user = ""
    return redirect(url_for('index'))


# for loop demo (check html)
@app.route('/receipe')
def users():
    ingredients = ['peanut butter', 'sugar', 'egg', 'vanilla']
    return render_template('butter_cookies.html', ingredients=ingredients)
