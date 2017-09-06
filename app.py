from gov.swagger import swagger_config, template
from gov.endpoints import (Health, Congress, CongressIds, Legislator,
    LegislatorName, LegislatorIds, LegislatorSocial, LegislatorBio,
    LegislatorTerm, LegislatorTerms, LegislatorTweet, LegislatorTweets)
from flask import Flask, jsonify, redirect
from flask_restful import Api, Resource
from flasgger import Swagger


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template=template, config=swagger_config)

api.add_resource(Health, '/api/health')

api.add_resource(Congress, '/api/congress',)
api.add_resource(CongressIds, '/api/congress/ids')

api.add_resource(Legislator, '/api/legislator/<string:id>')
api.add_resource(LegislatorName, '/api/legislator/<string:id>/name')
api.add_resource(LegislatorIds, '/api/legislator/<string:id>/id')
api.add_resource(LegislatorSocial, '/api/legislator/<string:id>/social')
api.add_resource(LegislatorBio, '/api/legislator/<string:id>/bio')
api.add_resource(LegislatorTerm, '/api/legislator/<string:id>/term')
api.add_resource(LegislatorTerms, '/api/legislator/<string:id>/terms')
api.add_resource(LegislatorTweet, '/api/legislator/<string:id>/tweet')
api.add_resource(LegislatorTweets, '/api/legislator/<string:id>/tweets')
# api.add_resource(LegislatorTweets, '/api/legislator/<string:id>/committees')


@app.route('/')
def index():
    return redirect('/api/spec/')

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Not found"}), 404


if __name__ == '__main__':
    app.run(debug=False, threaded=True)
