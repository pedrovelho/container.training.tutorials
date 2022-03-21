#!/usr/bin/env python
# encoding: utf-8
import os

from .healthz import healthz
from .keystore import EndPoints
from .server import FlaskAppWrapper
from .store import Store


def create_store():
    redis_host = os.environ.get("REDIS_HOST", "localhost")
    redis_port = os.environ.get("REDIS_PORT", "6379")
    redis_password = os.environ.get("REDIS_PASSWORD", "secret")

    return Store(
        redis_host=redis_host, redis_port=redis_port, redis_password=redis_password
    )


def main():
    debug = os.environ.get("DEBUG") != "false"
    store = create_store()
    endpoints = EndPoints(store)
    app = FlaskAppWrapper("crud-server")

    app.add_endpoint(
        endpoint="/healthz", endpoint_name="healthz", handler=healthz, methods=["GET"]
    )
    app.add_endpoint(
        endpoint="/keystore",
        endpoint_name="create",
        handler=endpoints.create,
        methods=["POST"],
    )
    app.add_endpoint(
        endpoint="/keystore/<id>",
        endpoint_name="read",
        handler=endpoints.read,
        methods=["GET"],
    )
    app.add_endpoint(
        endpoint="/keystore/<id>",
        endpoint_name="update",
        handler=endpoints.update,
        methods=["PUT"],
    )
    app.add_endpoint(
        endpoint="/keystore/<id>",
        endpoint_name="delete",
        handler=endpoints.delete,
        methods=["DELETE"],
    )

    app.run(host="0.0.0.0", debug=debug)


if __name__ == "__main__":
    main()
