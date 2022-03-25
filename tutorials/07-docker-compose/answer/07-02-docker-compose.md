As we saw on the last exercise to make this simple setup with 2 containers that communicate with each
other can get cumbersome. To improve things a docker-compose.yml file does all the network wiring for free.


```yaml
# The REDIS_PASSWORD must be set with for example
# export REDIS_PASSWORD=AStrongPassw0rd
# docker-compose up
version: "3.3"
services:

 redis:
    image: redis
    command: redis-server --requirepass "$REDIS_PASSWORD"
    hostname: "redis"
    volumes:
     - $PWD/redis-data:/var/lib/redis
     - $PWD/redis.conf:/usr/local/etc/redis/redis.conf

 keystore:
    build: rest-server
    environment:
      REDIS_HOST: "redis"
      REDIS_PORT: "6379"
      REDIS_PASSWORD: "$REDIS_PASSWORD"
    ports:
     - "80:5000"
```

Now to deploy the same complex service simply run docker-compose up -d.

```shell
# Start the containers
docker-compose up -d

# Check the service is working, no need for any network setup 
curl http://localhost:5000/healthz
#SUCCESS
 
# Now we can test a few curl calls
curl -X POST http://127.0.0.1:5000/keystore -H 'Content-Type: application-json' -d '{"key":"d1","value":"something"}'
#SUCCESS

# Add something to key d1
curl http://127.0.0.1:5000/keystore/d1 -H 'Content-Type: application-json'
#something

# Update key d1 with newvalue
curl -X PUT http://127.0.0.1:5000/keystore/d1 -H 'Content-Type: application-json' -d '{"value":"newvalue"}'
#SUCCESS

# Check the value associated with key d1 again
curl http://127.0.0.1:5000/keystore/d1 -H 'Content-Type: application-json'
#newvalue
```
