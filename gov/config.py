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
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/api/spec/",
    # "description": 'Endpoints for gov.vonapp.co/api/',
    'title': 'Government tweets',
    # 'endpoint': 'peeps',
}

template = {
  "swagger": "2.0",
  "info": {
    "title": "Government tweets",
    "description": "API endpoints for gov.vonapp.co",
    # "contact": {
      # "responsibleOrganization": "ME",
      # "responsibleDeveloper": "Me",
      # "email": "me@me.com",
      # "url": "www.me.com",
    # },
    # "termsOfService": "http://me.com/terms",
    "version": "0.1.0"
  },
  # "host": "127.0.0.1:5000",
  # "host": "gov.vonapp.co",  # overrides 127.0.0.1:5000
  "basePath": "/",  # base bash for blueprint registration
  "schemes": [
    # "https",
    # "https"
  ],
  "operationId": "get_data",
  # for tag order
  "tags": [
      {"name": "admin", "description": ""},
      {"name": "world", "description": ""},
  ]
}
