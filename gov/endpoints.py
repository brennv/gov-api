from .data import data, twitter_ids, tweets
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
          - admin
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


class WorldIds(Resource):
    def get(self):
        """
        Twitter handles
        ---
        tags:
          - world
        responses:
         200:
           description: Status check
           schema:
             id: Twitter
             properties:
               id:
                 type: string
                 description: Health status of API service
                 default: ok
        """
        return twitter_ids, 200


class WorldTweets(Resource):
    def get(self):
        """
        Tweets
        ---
        tags:
          - world
        responses:
         200:
           description: Status check
           schema:
             id: Tweets
             properties:
               id:
                 type: string
                 description: Health status of API service
                 default: ok
        """
        return tweets, 200
