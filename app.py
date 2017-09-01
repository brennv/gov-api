from gov import swagger_config, template
from gov import Health, Data, WorldIds, WorldTweets  # , UsIds, UsTweets
from flask import Flask
from flask_restful import Api, Resource
from flasgger import Swagger


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template=template, config=swagger_config)


api.add_resource(Health, '/api/health')
api.add_resource(Data, '/api/test')

api.add_resource(WorldIds, '/api/world/ids')
api.add_resource(WorldTweets, '/api/world/tweets')

# api.add_resource(UsIds, '/api/us/ids')
# api.add_resource(UsTweets, '/api/us/tweets')


if __name__ == '__main__':
    app.run(threaded=True)
