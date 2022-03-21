from keystore_rest_server.healthz import healthz


def test_create():
    assert healthz("")[0] == 200
