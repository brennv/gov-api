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
        Legislator entities
        ---
        tags:
          - congress
        responses:
         200:
           description: List of legislator entities
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
           description: List of legislator bioguide IDs
        """
        return congress_ids, 200


class Legislator(Resource):
    def get(self, id):
        """
        Legislator entity
        ---
        tags:
          - legislator
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: F000062
        responses:
         200:
           description: Legislator entity
        """
        return get_legislator(id), 200


class LegislatorName(Resource):
    def get(self, id):
        """
        Legislator name
        ---
        tags:
          - legislator
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: F000062
        responses:
         200:
           description: First, last and full name
        """
        return get_legislator(id, 'name'), 200


class LegislatorIds(Resource):
    def get(self, id):
        """
        Legislator IDs
        ---
        tags:
          - legislator
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: F000062
        responses:
         200:
           description: Associated legislator IDs
        """
        return get_legislator(id, 'id'), 200


class LegislatorSocial(Resource):
    def get(self, id):
        """
        Social accounts
        ---
        tags:
          - legislator
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: F000062
        responses:
         200:
           description: Social accounts
        """
        return get_legislator(id, 'social'), 200


class LegislatorBio(Resource):
    def get(self, id):
        """
        Biographical info
        ---
        tags:
          - legislator
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: F000062
        responses:
         200:
           description: Biographical info
        """
        return get_legislator(id, 'bio'), 200


class LegislatorTerm(Resource):
    def get(self, id):
        """
        Current term info
        ---
        tags:
          - legislator
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: F000062
        responses:
         200:
           description: Current office term info
        """
        return get_legislator(id, 'terms')[-1], 200


class LegislatorTerms(Resource):
    def get(self, id):
        """
        List of terms served
        ---
        tags:
          - legislator
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: F000062
        responses:
         200:
           description: Chronological list of terms
        """
        return get_legislator(id, 'terms'), 200


class LegislatorCommittees(Resource):
    def get(self, id):
        """
        Committee memberships
        ---
        tags:
          - legislator
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: F000062
        responses:
         200:
           description: List of committee memberships
        """
        return get_legislator(id, 'committees'), 200


class LegislatorTweet(Resource):
    def get(self, id):
        """
        Recent tweet
        ---
        tags:
          - legislator
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: F000062
        responses:
         200:
           description: Most recent tweet
        """
        return get_tweets(id, count=1), 200


class LegislatorTweets(Resource):
    def get(self, id):
        """
        List of recent tweets
        ---
        tags:
          - legislator
        parameters:
          - name: id
            in: path
            type: string
            required: true
            default: F000062
        responses:
         200:
           description: List of recent tweets
        """
        return get_tweets(id), 200
