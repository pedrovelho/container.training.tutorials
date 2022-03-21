import redis


class Store:
    def __init__(self, redis_host="localhost", redis_port=6379, redis_password=""):
        self.r = redis.Redis(
            host=redis_host,
            port=redis_port,
            password=redis_password,
        )

    def set(self, key, value):
        self.r.set(key, value)

    def get(self, key):
        r = self.r.get(key)
        if r is None:
            raise KeyError(key)
        return r.decode()

    def pop(self, key):
        self.r.delete(key)
