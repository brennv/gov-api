from config import swagger_config, template
from endpoints import (Health, Data)
from flask import Flask
from flask_restful import Api, Resource
from flasgger import Swagger


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app, template=template, config=swagger_config)

api.add_resource(Data, '/api/data')
api.add_resource(Health, '/api/health')


if __name__ == '__main__':
    app.run(threaded=True)  # debug=True
