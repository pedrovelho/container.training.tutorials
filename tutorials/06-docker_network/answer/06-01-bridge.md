We are going to show step-by-step how to reach your VM using the docker bridge associated IP.

```shell
# Dump the bridge network details
docker network inspect bridge
#[
#    {
#        "Name": "bridge",
#        "Id": "931a6c79d400c8f85cfeaa480db0915a3643d2fec1b5520a84c768244078889e",
#...
#        "Containers": {
#            "6e8e8f3cf2ac540146074e46dee726a7ba8ef20380463cd7e911d2386184b0e0": {
#                "Name": "wizardly_boyd",
#                "EndpointID": "614ec8b4bf03e6d80044a9258f54482a6a3fb86bceefbbe01412f12cd074b261",
#                "MacAddress": "02:42:ac:12:00:02",
#                "IPv4Address": "172.18.0.2/16",
#                "IPv6Address": ""
#            }
#        },
#...
#    }
#]

# Another method to discover the bridge IP associated with your container is to docker container inspect
docker container inspect wizardly_boyd | jq -r '.[0].NetworkSettings.Networks.bridge.IPAddress'
#172.18.0.2

# Alternatively, you can use the --format option, and the container short id instead of the name
docker container inspect 6e8 --format '{{json .NetworkSettings.Networks.bridge.IPAddress}}'
#"172.18.0.2"

# Let's try to reach the container
ping 172.18.0.2
#PING 172.18.0.2 (172.18.0.2) 56(84) bytes of data.
#64 bytes from 172.18.0.2: icmp_seq=1 ttl=64 time=0.060 ms
#64 bytes from 172.18.0.2: icmp_seq=2 ttl=64 time=0.072 ms
#64 bytes from 172.18.0.2: icmp_seq=3 ttl=64 time=0.045 ms

# Also if you did run the healthz container from before you can reach it by using curl
curl -v http://172.18.0.2:8080/healthz
#*   Trying 172.18.0.2:8080...
#...
#< HTTP/1.1 200 OK
#...
#* Connection #0 to host 172.18.0.2 left intact
```
