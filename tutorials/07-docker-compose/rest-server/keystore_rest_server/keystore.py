import json


class EndPoints:
    def __init__(self, store):
        self.store = store

    def create(self, request):
        try:
            print(request)
            print(request.data)
            record = json.loads(request.data)
            print(f"CREATE {record}")
            self.store.set(record["key"], record["value"])
        except json.decoder.JSONDecodeError as err:
            print(f"Problems with your json {err}")
            return 500, "ERROR: Parsing json"
        return 200, "SUCCESS"

    def read(self, id, request=None):
        print(f"READ {id}")
        try:
            r = self.store.get(id)
            print(f"Read {r}")
            return 200, r
        except KeyError:
            return 500, f"Key {id} not found on storage"

    def update(self, id, request):
        record = json.loads(request.data)
        self.store.set(id, record["value"])
        print(f"UPDATE {id} WITH {record}")
        return 200, "SUCCESS"

    def delete(self, id, request=None):
        print(f"DELETE {id}")
        self.store.pop(id)
        return 200, "SUCCESS"
