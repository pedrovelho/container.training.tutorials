Let's use an image that has ping available for convinience.

```shell
docker run -d --name server willfarrell/ping

# Test the container with ping
docker exec server ping localhost

# Now create a new server
docker run -d --name server2 willfarrell/ping

# Let's try to ping server from server2
docker exec server2 ping server
#ping: bad address 'server'

# As we can see the name server does not resolve, this is because of bridge network

# Now we create a new network
docker network create mynet
#cc2381bdb0f800f20ebd43fa6e9b514ccdd709f654cabd13e546f7b16461bedf

# Then we connect both server and server2 to this network
docker network connect mynet server
docker network connect mynet server2

# Let's try the ping command again
docker exec server2 ping server
#PING server (172.21.0.2): 56 data bytes
#64 bytes from 172.21.0.2: seq=0 ttl=64 time=0.124 ms
#64 bytes from 172.21.0.2: seq=1 ttl=64 time=0.108 ms
#^C

# So server2 resolves server one, but can server resolve server2?
docker exec server ping server2
#PING server2 (172.21.0.3): 56 data bytes
#64 bytes from 172.21.0.3: seq=0 ttl=64 time=0.122 ms
#64 bytes from 172.21.0.3: seq=1 ttl=64 time=0.117 ms
```
