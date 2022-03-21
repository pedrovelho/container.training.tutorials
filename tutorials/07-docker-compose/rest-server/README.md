
# rest-server

A simple rest-server to practice container and CI skills.

```shell
GET /healthz # retrieve health information, 200 means working
POST /keystore # create a new random i
GET /keystore/<id>
PUT /keystore/<id>
DELETE /keystore/<id>

```

## Requirements

Install python, and basic build tools, also install unzip and wget for convenience.

```shell
sudo apt-get update
sudo apt-get install -y python3-dev python3-pip
```

Install required python dependencies.

```shell
pip3 install redis flask pytest
```


## Install

Get the code from github.

```shell
git clone https://github.fixme
# change the working directory
cd rest-server
```

## Running

For running the application you will need a redis instance. You can make a fast redis running instance by using
the dockerhub image available.

```shell
docker run -d redis:latest --requirepass "mysecretpass"
```

After you can check the container ip and port by using.

```shell
docker container inspect upbeat_chaum | jq -r '.[0].NetworkSettings.IPAddress'
#172.18.0.3


docker container inspect upbeat_chaum | jq -r '.[0].NetworkSettings.Ports'
#{
#  "6379/tcp": null
#}
```

Now set the environment variables to match your redis server.

```shell
export REDIS_HOST="172.18.0.3"
export REDIS_PORT="6379"
export REDIS_PASSWORD="mysecretpass"
```

Run the application on the background.

```shell
python3 ./main.py 
# * Serving Flask app 'crud-server' (lazy loading)
# * Environment: production
#   WARNING: This is a development server. Do not use it in a production deployment.
#   Use a production WSGI server instead.
# * Debug mode: on
# * Running on all addresses.
#   WARNING: This is a development server. Do not use it in a production deployment.
# * Running on http://172.17.0.6:5000/ (Press CTRL+C to quit)
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 178-837-042
```

## Testing

To see the application working you can access the local URL that is advertised.

```shell
curl http://172.17.0.6:5000/healthz
#172.17.0.6 - - [17/Mar/2022 14:40:48] "GET /healthz HTTP/1.1" 200 -
```

Another simple test, add and retrieve a value.

```shell
# Check key d1 is not there
curl http://127.0.0.1:5000/keystore/d1 -H 'Content-Type: application-json'
#READ d1
#127.0.0.1 - - [17/Mar/2022 14:43:22] "GET /keystore/d1 HTTP/1.1" 500 -

# Add a new key d1 with value something
curl -X POST http://127.0.0.1:5000/keystore -H 'Content-Type: application-json' -d '{"key":"d1","value":"something"}'
#<Request 'http://127.0.0.1:5000/keystore' [POST]>
#b'{"key":"d1","value":"something"}'
#CREATE {'key': 'd1', 'value': 'something'}
#127.0.0.1 - - [17/Mar/2022 14:43:49] "POST /keystore HTTP/1.1" 200 -

# Check the values of key d1
curl http://127.0.0.1:5000/keystore/d1 -H 'Content-Type: application-json'
#READ d1
#Read something
#127.0.0.1 - - [17/Mar/2022 14:44:19] "GET /keystore/d1 HTTP/1.1" 200 -
```

Execute all tests, make sure the application is running and environment variables to access redis service
are correctly set.

```shell
pytest .
```

## Tips

You can  run exposing the port 6397 in this case set redis host to localhost, and port to 6397.

```shell
# Run the redis container
docker run --name redis-4-keystore -p 6397:6397 -d redis:latest --requirepass "mysecretpass"

# In this case set the REDIS_HOST env var to localhost
export REDIS_HOST="localhost"
```