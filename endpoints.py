from data import data, twitter_ids, tweets
from flask_restful import Resource


class Health(Resource):
    def get(self):
        """
        API health check
        ---
        tags:
          - admin
        responses:
         200:
           description: Status check
           schema:
             id: Status
             properties:
               status:
                 type: string
                 description: Health status of API service
                 default: ok
        """
        return {'status': 'ok'}, 200


class Data(Resource):
    def get(self):
        """
        All the data
        ---
        tags:
          - all the data
        responses:
         200:
           description: Status check
           schema:
             id: Data
             properties:
               id:
                 type: string
                 description: Health status of API service
                 default: ok
        """
        return data, 200

"""


@app.route('/api/twitter')
def twitter_handles():
    return jsonify(twitter_ids)


@app.route('/api/tweets')
def tweets():
    return jsonify(tweets)
"""
