import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
from collections import Counter
from wordcloud import WordCloud
import os 




stopWords = set(stopwords.words('english'))


def read_timeline_json(json_file):
    tweets = []
    for line in json_file:
        tweet = json.loads(line)
        tweets.append(tweet)
    return tweets

def process(text, stopwords):   
    tokenizer = TweetTokenizer()
    text = text.lower()
    tokens = tokenizer.tokenize(text)
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit() 
           and tok.isalpha()]

def get_token(tweets):
    list_token = []
    tf = Counter()
    for tweet in tweets:
        tokens = process(text=tweet.get('text', ''),
                    stopwords=stopWords)
        if len(tokens) != 0:
            list_token.append(tokens)
    return list_token

def tf_idf(tokens, top_count):
    tf = Counter()
    for token in tokens:
        tf.update(token)

    most_common = tf.most_common(top_count)
    # convert tuple to list
    most_common = list(list(i) for i in most_common )
    return most_common

def generate_wordcloud(tokens, filename, save_path):
    # flatten the list to get lit of words
    words = [item for sublist in tokens for item in sublist]
    wordcloud = WordCloud(stopwords=stopWords, background_color='white', width=900, height=1000).generate(' '.join(words))
    fname = "wordcloud_{}.png".format(filename)
    save_path = os.path.join(save_path, fname)
    wordcloud.to_file(save_path)


    return fname

