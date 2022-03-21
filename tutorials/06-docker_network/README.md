# Making your own networks

We have not yet dig into the world of docker networks. Throughout this tutorial we will see the different
commands and aspect of docker network. To start install net-tools, so you have access to ifconfig.

```shell
sudo apt-get install net-tools
#Reading package lists... Done
#Building dependency tree       
#Reading state information... Done
#net-tools is already the newest version (1.60+git20180626.aebd88e-1ubuntu1).
#0 upgraded, 0 newly installed, 0 to remove and 12 not upgraded.
```

Now remove all your docker containers and check which networks are available on your VM.

```shell
# Verify all containers are gone
docker ps -a
# CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

# Check available network interfaces
ifconfig
#docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
#        inet 172.18.0.1  netmask 255.255.0.0  broadcast 172.18.255.255
#        inet6 fe80::42:1dff:fea6:c977  prefixlen 64  scopeid 0x20<link>
#        ether 02:42:1d:a6:c9:77  txqueuelen 0  (Ethernet)
#        RX packets 16511  bytes 1235310 (1.2 MB)
#        RX errors 0  dropped 0  overruns 0  frame 0
#        TX packets 24667  bytes 714594387 (714.5 MB)
#        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
#
#eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#        inet 172.17.0.6  netmask 255.255.255.0  broadcast 172.17.0.255
#        inet6 fe80::6245:bdff:fe0f:bb7d  prefixlen 64  scopeid 0x20<link>
#        ether 60:45:bd:0f:bb:7d  txqueuelen 1000  (Ethernet)
#        RX packets 2944872  bytes 2148862213 (2.1 GB)
#        RX errors 0  dropped 0  overruns 0  frame 0
#        TX packets 2170924  bytes 604270278 (604.2 MB)
#        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
#
#lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
#        inet 127.0.0.1  netmask 255.0.0.0
#        inet6 ::1  prefixlen 128  scopeid 0x10<host>
#        loop  txqueuelen 1000  (Local Loopback)
#        RX packets 2272  bytes 258408 (258.4 KB)
#        RX errors 0  dropped 0  overruns 0  frame 0
#        TX packets 2272  bytes 258408 (258.4 KB)
#        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

As you can see besides `eth0` and loopback network adapters there is a new one called `docker0`. `docker0` is the
adapter that docker uses to create routes from your VM to the contaners on the default bridge mode. 
Check the available routes.

```shell
ip route
#default via 172.17.0.1 dev eth0 proto dhcp src 172.17.0.6 metric 100 
#168.63.129.16 via 172.17.0.1 dev eth0 proto dhcp src 172.17.0.6 metric 100 
#169.254.169.254 via 172.17.0.1 dev eth0 proto dhcp src 172.17.0.6 metric 100 
#172.17.0.0/24 dev eth0 proto kernel scope link src 172.17.0.6 
#172.18.0.0/16 dev docker0 proto kernel scope link src 172.18.0.1 linkdown 
```


As we can see there is a convenient route that specify `docker0` ip as the gateway for network `172.18.x.y`.
This means all packages that we direct to an ip starting by 172.18 will be redirected to the `docker0` interface.
Now let's see what happens when we add one container.

```shell
# Start a container, might be a different one
docker run -dti -p 80:8080 alpine:healthz-optimized

# Verify the container is running
docker ps -a
#CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS          PORTS                                   NAMES
#6e8e8f3cf2ac   alpine:healthz-optimized   "/usr/local/bin/pyth…"   19 seconds ago   Up 15 seconds   0.0.0.0:80->8080/tcp, :::80->8080/tcp   wizardly_boyd

# Check the available network interfaces
ifconfig
#docker0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
# ... suppressed eth0 and lo for the sake of brevity
#        inet 172.18.0.1  netmask 255.255.0.0  broadcast 172.18.255.255
#        inet6 fe80::42:1dff:fea6:c977  prefixlen 64  scopeid 0x20<link>
#        ether 02:42:1d:a6:c9:77  txqueuelen 0  (Ethernet)
#        RX packets 16511  bytes 1235310 (1.2 MB)
#        RX errors 0  dropped 0  overruns 0  frame 0
#        TX packets 24669  bytes 714594607 (714.5 MB)
#        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
#
#vethf69821a: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#        inet6 fe80::7cca:4dff:fe44:faea  prefixlen 64  scopeid 0x20<link>
#        ether 7e:ca:4d:44:fa:ea  txqueuelen 0  (Ethernet)
#        RX packets 0  bytes 0 (0.0 B)
#        RX errors 0  dropped 0  overruns 0  frame 0
#        TX packets 11  bytes 946 (946.0 B)
#        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

We can see that a new network interface was created and this interface associated an ipv6. To further understand
we can now check the docker available networks.

```shell
# See the available network on docker, bridge is used by default
docker network ls
#NETWORK ID     NAME      DRIVER    SCOPE
#931a6c79d400   bridge    bridge    local
#ab5eafcd12b0   host      host      local
#0b0507b996f8   none      null      local
```

## **Exercise**: Try to reach your container by using the docker given ip

Inspect the docker network to find your container ip on the docker bridge subnet, you can either inspect 
the container object as well. 
What is the IP associated with the container? Can you reach the container using that ip?

> See the [solution](./answer/06-01-bridge.md)

## **Exercise**: Create a subnetwork.

Create a subnetwork. Are there any new interfaces that appear? Are the routes on your ip table the same?
Create a container on that network, what route interfaces change can you see?

> See the [solution](./answer/06-02-single_adapter.md)

## **Exercise**: Containers on the same network.

Create 2 containers using the default bridge network. Can you ping one container from another?
Can we use their names instead of IPs?

> See the [solution](answer/06-03-multi_adapter.md)

## **Exercise**: Containers on different networks.

Create 2 different networks and start one container in each. Now can you 
find their name resolution.

> See the [solution](./answer/06-03-different_networks.md)
