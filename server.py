import falcon

from endpoints import EREndpoints

app = falcon.API()
EREndpoints().initialize_endpoints(app)

