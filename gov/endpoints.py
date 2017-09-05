from .data import (congress, congress_ids, get_legislator, get_tweets)
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


class Congress(Resource):
    def get(self):
        """
        Legislator objects
        ---
        tags:
          - congress
        responses:
         200:
           description: Legislator objects
           schema:
             id: Data
             properties:
               id:
                 type: string
                 description: Health status of API service
                 default: ok
        """
        return congress, 200


class CongressIds(Resource):
    def get(self):
        """
        Legislator IDs
        ---
        tags:
          - congress
        responses:
         200:
           description: Legislator bioguide IDs
           schema:
             id: Data
             properties:
               id:
                 type: string
                 description: Health status of API service
                 default: ok
        """
        return congress_ids, 200


class Legislator(Resource):
    def get(self, id):
        """
        Legislator object
        ---
        tags:
          - legislator
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
        return get_legislator(id), 200


class LegislatorName(Resource):
    def get(self, id):
        """
        Legislator names
        ---
        tags:
          - legislator
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
        return get_legislator(id, 'name'), 200


class LegislatorIds(Resource):
    def get(self, id):
        """
        All the data
        ---
        tags:
          - legislator
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
        return get_legislator(id, 'id'), 200


class LegislatorSocial(Resource):
    def get(self, id):
        """
        All the data
        ---
        tags:
          - legislator
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
        return get_legislator(id, 'social'), 200


class LegislatorBio(Resource):
    def get(self, id):
        """
        All the data
        ---
        tags:
          - legislator
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
        return get_legislator(id, 'bio'), 200


class LegislatorTerm(Resource):
    def get(self, id):
        """
        All the data
        ---
        tags:
          - legislator
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
        return get_legislator(id, 'terms')[-1], 200


class LegislatorTerms(Resource):
    def get(self, id):
        """
        All the data
        ---
        tags:
          - legislator
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
        return get_legislator(id, 'terms'), 200


class LegislatorCommittees(Resource):
    def get(self, id):
        """
        All the data
        ---
        tags:
          - legislator
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
        return get_legislator(id, 'committees'), 200


class LegislatorTweets(Resource):
    def get(self, id):
        """
        All the data
        ---
        tags:
          - legislator
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
        return get_tweets(id), 200
