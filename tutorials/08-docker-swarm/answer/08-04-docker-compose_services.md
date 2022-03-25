Lets create a simple service.

```shell
# First we need to puth our image available on an external registry, so let's use dockerhub as before
# Tag the image properly for dockerhub, <youruser>/<image_name>:<image_tag>
docker tag rest-server:latest letrololo/rest-server:latest

# Now push the image
docker push letrololo/rest-server
#Using default tag: latest
#The push refers to repository [docker.io/letrololo/rest-server]
#251bbc052cbb: Pushed 
#ea822f1ace57: Pushed 
#b8de1040f39c: Pushed 
#5cd508ed4152: Mounted from library/python 
#e983774ec12e: Mounted from library/python 
#b43c28bae2f5: Mounted from library/python 
#f502a2b61672: Mounted from library/python 
#346fddbbb0ff: Mounted from library/python 
#latest: digest: sha256:83be1ced1be53eb04de7c950647a35c7fd862d71e74e09c031b933f00289043c size: 1996


# Now just use stack deploy/up to create the services on the swarm
# Remember to define the REDIS_PASSWORD environment variable before launching
docker stack up -c ./docker-stack.yml keystore
#Ignoring unsupported options: build
#
#Creating network keystore_default
#Creating service keystore_redis
#Creating service keystore_keystore

# If the command fails you can always undeploy the entiry stack using docker stack down
docker stack down keystore
#Removing service keystore_keystore
#Removing service keystore_redis
#Removing network keystore_default

# You can verify that the stack is running correctly
docker stack ps keystore
#ID             NAME                  IMAGE                          NODE                         DESIRED STATE   CURRENT STATE           ERROR     PORTS
#ospxcbg8dgms   keystore_keystore.1   letrololo/rest-server:latest   sparks-docker-admin-worker   Running         Running 2 minutes ago             
#9z123ugtmsmf   keystore_redis.1      redis:6.2.6-alpine             sparks-docker-admin          Running         Running 2 minutes ago  

# Check the services associated
docker stack services keystore
#ID             NAME                MODE         REPLICAS   IMAGE                          PORTS
#nwuylugjp577   keystore_keystore   replicated   1/1        letrololo/rest-server:latest   *:5000->5000/tcp
#b3mt7brvmg0e   keystore_redis      replicated   1/1        redis:6.2.6-alpine             *:6379->6379/tcp

# Finally we can execute curl commands on the worker node (becuase is where rest-server is running)
# Note that the communication from rest-server to redis works through the overlay network and accord nodes
curl -X POST http://127.0.0.1:5000/keystore -H 'Content-Type: application-json' -d '{"key":"d1","value":"someasdfasdfas"}'
#SUCCESS
curl  http://localhost:5000/keystore/d1
#someasdfasdfas
```

The `docker-stack.yml` have the following content. 

```yaml
# docker stack up -c docker-stack.yml
version: "3.9"
services:

 redis:
    image: redis
    command: redis-server --requirepass "0sG098kaKil"
    hostname: "redis"
    ports:
     - "6379:6379"
    volumes:
     - /home/azureuser/redis-data:/var/lib/redis
     - /home/azureuser/redis.conf:/usr/local/etc/redis/redis.conf

 keystore:
    image: "letrololo/rest-server:latest"
    environment:
      REDIS_HOST: "redis"
      REDIS_PORT: "6379"
      REDIS_PASSWORD: "0sG098kaKil"
    ports:
     - "5000:5000"
```








