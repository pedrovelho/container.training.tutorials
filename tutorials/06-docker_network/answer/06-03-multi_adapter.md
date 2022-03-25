Let's create a total of 4 hosts. Each pair on a different network.

```shell
# Assumming we already have server and server2 on mynet
# We create s3 and s4 and attach those to new network called secondnet
docker run -d --name s3 willfarrell/ping 
#920b5c8a948785e20f84eafdbc469fe63e24e5bdcd85860fd7c76a1cc32b0d6e
docker run -d --name s4 willfarrell/ping 
#2a6f60301815688d9d01c87915b0f4610393c67516acdf5a77ab20d56ef477ab

# Now let's test connectivity
docker network create secondnet
395f2af43be26b4727338d6b40229e0d1c1117e69cf68d3828bf862722dfb0e8

# Attach secnodnet to s3 and s4
docker network connect secondnet s3
docker network connect secondnet s4

# Then we check that s3 resolve s4 and vice-versa
docker exec s3 ping s4
#PING s4 (172.22.0.3): 56 data bytes
#64 bytes from 172.22.0.3: seq=0 ttl=64 time=0.230 ms

docker exec s4 ping s3
#PING s3 (172.22.0.2): 56 data bytes
#64 bytes from 172.22.0.2: seq=0 ttl=64 time=0.072 ms


# However, the s4 cannot see server
docker exec s4 ping server
#ping: bad address 'server'

# To resovle that issue we need to attach s4 also to mynet
docker network connect mynet s4
docker exec s4 ping server.mynet
#PING server.mynet (172.21.0.2): 56 data bytes
#64 bytes from 172.21.0.2: seq=0 ttl=64 time=0.131 ms

docker exec s4 ping server
#PING server (172.21.0.2): 56 data bytes
#64 bytes from 172.21.0.2: seq=0 ttl=64 time=0.190 ms


# Note that server also sees s4, but only through mynet
docker exec server ping s4
#PING s4 (172.21.0.4): 56 data bytes
#64 bytes from 172.21.0.4: seq=0 ttl=64 time=0.121 ms

docker exec server ping s4.secondnet
#ping: bad address 's4.secondnet'

docker exec server ping s4.mynet
#PING s4.mynet (172.21.0.4): 56 data bytes
#64 bytes from 172.21.0.4: seq=0 ttl=64 time=0.143 ms
```
