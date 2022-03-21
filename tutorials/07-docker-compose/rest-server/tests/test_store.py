from pytest import fixture

from keystore_rest_server.main import create_store


@fixture
def store():
    return create_store()


def test_set(store):
    store.set("1", "test")
    assert store.get("1") == "test"


def test_delete(store):
    store.set("1", "test")
    assert store.get("1") == "test"
    store.pop("1")
    try:
        store.get("1")
    except KeyError:
        pass
    else:
        raise Exception("Not deleted")
