import pytest

from keystore_rest_server.keystore import EndPoints
from keystore_rest_server.store import Store


class MockRequest:
    def __init__(self, data=None):
        self.data = data


class MockStore(Store):
    def __init__(self):
        self.storage = {}

    def set(self, key, value):
        self.storage[str(key)] = value

    def get(self, key):
        return self.storage[str(key)]

    def pop(self, key):
        self.storage.pop(str(key))


@pytest.fixture(scope="session")
def endpoint():
    return EndPoints(MockStore())


def test_create(endpoint):
    assert endpoint.create(MockRequest('{ "key" : "1", "value": "chubbs" }'))[0] == 200


def test_read(endpoint):
    endpoint.create(MockRequest('{ "key" : "1", "value": "chubbs" }'))
    assert endpoint.read(1) == (200, "chubbs")


def test_update(endpoint):
    endpoint.create(MockRequest('{ "key" : "1", "value": "chubbs" }'))
    endpoint.update(1, MockRequest('{ "key" : "1", "value": "chubbinho" }'))
    assert endpoint.read(1) == (200, "chubbinho")


def test_delete(endpoint):
    endpoint.create(MockRequest('{ "key" : "1", "value": "chubbs" }'))
    endpoint.delete(1)
    assert endpoint.read(1)[0] == 500
