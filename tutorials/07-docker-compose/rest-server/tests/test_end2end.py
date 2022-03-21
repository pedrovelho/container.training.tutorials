import requests


def test_create_read():
    # create
    # curl - X POST http://127.0.0.1:5000/create -H 'Content-Type: application-json' - d '{"key":"d1","value":"something"}'
    r = requests.post(
        "http://localhost:5000/keystore", data='{"key": "1", "value":"something"}'
    )
    assert r.status_code == 200
    # read
    r = requests.get("http://localhost:5000/keystore/1")
    assert r.status_code == 200
    # assert read == excpected
    assert r.text == "something"


def test_create_update_read():
    # curl - X POST http://127.0.0.1:5000/create -H 'Content-Type: application-json' - d '{"key":"d1","value":"something"}'
    r = requests.post(
        "http://localhost:5000/keystore", data='{"key": "1", "value":"something"}'
    )
    assert r.status_code == 200
    # update
    r = requests.put(
        "http://localhost:5000/keystore/1", data='{"value":"newsomething"}'
    )
    assert r.status_code == 200
    r = requests.get("http://localhost:5000/keystore/1")
    assert r.status_code == 200
    assert r.text == "newsomething"


def test_create_delete():
    # read
    r = requests.get("http://localhost:5000/keystore/1")
    assert r.status_code == 200
    # delete
    r = requests.delete("http://localhost:5000/keystore/1")
    assert r.status_code == 200
    # read
    r = requests.get("http://localhost:5000/keystore/1")
    assert r.status_code == 500
