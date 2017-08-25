from data import data, twitter_ids, tweets
from flask import Flask, jsonify


app = Flask(__name__)
all_data = [v for k, v in data.items()]


@app.route('/gov/api/')
def all_the_data():
    return jsonify(all_data)


@app.route('/gov/api/twitter')
def twitter_handles():
    return jsonify(twitter_ids)


@app.route('/gov/api/tweets')
def tweets():
    return jsonify(tweets)


if __name__ == '__main__':
    app.run(debug=True)
