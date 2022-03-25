First let's create a docker secret using a random string as the password.

```shell
# Create a random secret for redis, call it redispass
base64 /dev/urandom | head -c16 | docker secret create redispass -
#ke89wstkead2vbvj8g4s8l94z

docker secret ls
#ID                          NAME        DRIVER    CREATED         UPDATED
#ke89wstkead2vbvj8g4s8l94z   redispass             2 minutes ago   2 minutes ago
```

The secret need to relay the services, so we need to edit the docker-stack.yml file and add the secret.
We need to use `external: true` so it is resolved by docker. We need to import the secret on each 
service. When correctly configure the secret will appear in `/run/secrets/<secretname>`. Then, we need
to use this file to feed the `--requirepassowrd` option on redis and environment variable `REDIS_PASSWORD`
for the keystore service.

```yaml
# docker stack up -c docker-compose-stack.yml
version: "3.9"

secrets:
  redissecret:
    external: true
    name: redispass

services:
 redis:
    secrets:
      - redissecret
    image: redis
    # This is tricky to find, thanks to the redis team
    # https://github.com/docker-library/redis/issues/46#issuecomment-335326234
    command: [
      "bash", "-c",
      '
       docker-entrypoint.sh
       --requirepass "$$(cat /run/secrets/redissecret)"
      '
    ]
    hostname: "redis"
    ports:
     - "6379:6379"
    volumes:
     - /home/azureuser/redis-data:/var/lib/redis
     - /home/azureuser/redis.conf:/usr/local/etc/redis/redis.conf

 keystore:
    image: "letrololo/rest-server:latest"
    secrets:
      - redissecret
    command: [
      "bash", "-c",
      '
       REDIS_PASSWORD="$$(cat /run/secrets/redissecret)"
       python3 main.py
      '
    ]
    environment:
      REDIS_HOST: "redis"
      REDIS_PORT: "6379"
    ports:
     - "5000:5000"
```
