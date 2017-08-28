from data import data, twitter_ids, tweets
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def health():
    return 'API/ up'


@app.route('/api/')
def all_the_data():
    return jsonify(data)


@app.route('/api/twitter')
def twitter_handles():
    return jsonify(twitter_ids)


@app.route('/api/tweets')
def tweets():
    return jsonify(tweets)


if __name__ == '__main__':
    app.run(threaded=True)
