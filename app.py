from gov import swagger_config, template
from gov import Health, Data, Twitter, Tweets
from flask import Flask
from flask_restful import Api, Resource
from flasgger import Swagger


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template=template, config=swagger_config)


api.add_resource(Health, '/api/health')
api.add_resource(Data, '/api/test')
api.add_resource(Twitter, '/api/world/ids')
api.add_resource(Tweets, '/api/world/tweets')


if __name__ == '__main__':
    app.run(threaded=True)
