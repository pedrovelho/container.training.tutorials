A complex docker build file would as follows.

```shell
# Use a full image version
FROM python:3.9.2-slim as base

# Create a builder container
FROM base as builder

# System deps:
RUN apt-get update && apt-get install -y python3-dev python3-pip
RUN pip3 install --prefix=/runtime --force-reinstall redis flask pytest

# Use the base container and only copy the runtime + the app
FROM base as runtime
COPY --from=builder /runtime /usr/local
COPY ./main.py /app/
COPY keystore_rest_server /app/keystore_rest_server/

WORKDIR /app

# Set env and metadata
EXPOSE 5000
MAINTAINER pedro.velho@ryax.tech

CMD python3 ./main.py
```


To test the dockerfile generate the image with docker build.

```shell
cd rest-server
docker build -t rest-server . -f Dockerfile.multi
#...
#Step 15/15 : CMD ./main.py
# ---> Running in dbc30692d93b
#Removing intermediate container dbc30692d93b
# ---> e0e9d4ff2d2f
#Successfully built e0e9d4ff2d2f
#Successfully tagged rest-server:latest

# To test this let's first create a redis service if not running yet
# Don't need to publish the port externally
docker run --name redis-4-keystore -d redis:latest --requirepass "mysecretpass"
#Unable to find image 'redis:latest' locally
#latest: Pulling from library/redis
#f7a1c6dad281: Pull complete 
#c5f81eaec564: Pull complete 
#2be237d3defa: Pull complete 
#1640a11de2e5: Pull complete 
#9138edee9512: Pull complete 
#c62664237d8c: Pull complete 
#Digest: sha256:21464f430bd61dfe5d5782fcad0ff66e60ae49998351fc0899d4d2f815079c44
#Status: Downloaded newer image for redis:latest
#398391c88a6898fe22d08a3ce16ac02ef303e146e349f0b3005b87b1e3a7b31e

# Now let's launch our image with the correct environment variables
docker run -d --name rest-server-ctn \
  -e REDIS_HOST="redis-4-keystore" \
  -e REDIS_PORT="6379" \
  -e REDIS_PASSWORD="mysecretpass" \
  -p 5000:5000 \
  rest-server

# Check the service is working 
curl http://localhost:5000/healthz
#SUCCESS

# Now to make the 2 containers communicate we need to create a network
docker network create mynet

# And attach this network to both containers so the host redis-4-keystore is resolved on the rest-server
docker network connect mynet rest-server-ctn 
docker network connect mynet redis-4-keystore
  
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