### Second Flask application - Dynamic HTMl in templates###
from flask import Flask, render_template
import os 
from tweet_processing import *


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
FILES_STATIC = os.path.join(APP_STATIC, 'files')


@app.route('/')
def index():
    # store under templates folder
    return render_template("index.html")


# read user_timeline from from static/files directory. 
@app.route("/timeline/<filename>")
def user(filename):
    file_dir = "user_timeline_{}.json".format(filename)
    with open(os.path.join(FILES_STATIC, file_dir)) as f:
        tweets = read_timeline_json(f)
        tokens = get_token(tweets)
        top_tf_idf = tf_idf(tokens, 10)
        top_tf_idf = [['Word', 'Frequency']] + top_tf_idf

        wordcloud_fname = generate_wordcloud(tokens, filename, FILES_STATIC)

    return render_template("index.html", tfidf=top_tf_idf, user=filename, wordcloud=wordcloud_fname)
