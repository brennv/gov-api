from data import data, handles, tweets
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/gov/api/congress')
def congress():
    return jsonify(data)


@app.route('/gov/api/congress/handles')
def congress_handles():
    return jsonify(handles)


@app.route('/gov/api/congress/tweets')
def congress_tweets():
    return jsonify(tweets)


if __name__ == '__main__':
    app.run(debug=True)
