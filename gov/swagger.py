import os

host = os.getenv('GOV_API_HOST', '127.0.0.1:5000')
scheme = [os.getenv('GOV_API_SCHEME', '')]
scheme = [x for x in scheme if x]

template = {
  # "host": "gov.vonapp.co",
  "host": host,
  # "schemes": ["https"],
  "schemes": scheme,
  "swagger": "2.0",
  "info": {
    "title": "Government tweets",
    "description": "API endpoints for gov.vonapp.co",
    "version": "0.1.0"
  },
  "basePath": "/",
  "operationId": "get_data",
  # set tag order
  "tags": [
      {"name": "admin", "description": ""},
      {"name": "congress", "description": ""},
      {"name": "legislator", "description": ""},
  ]
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'spec',
            "name": 'gov',
            "route": '/api/spec.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/api/spec/",
    'title': 'Government tweets',
}
