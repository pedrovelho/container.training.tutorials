from flask import Flask, Response, request


class EndpointAction(object):
    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args, **kwargs):
        kwargs["request"] = request
        status, response = self.action(*args, **kwargs)
        self.response = Response(status=status, headers={}, response=response)
        return self.response


class FlaskAppWrapper(object):
    app = None

    def __init__(self, name):
        self.app = Flask(name)

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

    def add_endpoint(
        self, endpoint=None, endpoint_name=None, handler=None, methods=None
    ):
        self.app.add_url_rule(
            endpoint, endpoint_name, EndpointAction(handler), methods=methods
        )
