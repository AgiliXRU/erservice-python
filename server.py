import falcon

from endpoints import EREndpoints

app = falcon.App(cors_enable=True)
EREndpoints().initialize_endpoints(app)

