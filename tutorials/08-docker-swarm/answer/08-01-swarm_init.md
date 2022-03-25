On your first docker server initialize swarm mode. WARNING, just do swarm init in a single node.

```shell
docker swarm init
#Swarm initialized: current node (i05ivyhuaas9e19xr1hlmyjm9) is now a manager.
#
#To add a worker to this swarm, run the following command:
#
#    docker swarm join --token SWMTKN-1-5v8ourkgbb6r9pke6zmyek9ayj38tmfku8e4vlrjsgf25wxuyg-8vsmb51juwtvlw5mt7wk9npfw 172.17.0.6:2377
#
#To add a manager to this swarm, run 'docker swarm join-token manager' and follow the instructions.
```

We can check we are in swarm mode by issuing docker info. On the server section we can see `Swarm: active` as well
as several other swarm related parameters.

```shell
docker info
#Client:
# Context:    default
# Debug Mode: false
# Plugins:
#  app: Docker App (Docker Inc., v0.9.1-beta3)
#  buildx: Docker Buildx (Docker Inc., v0.8.0-docker)
#  scan: Docker Scan (Docker Inc., v0.17.0)
#
#Server:
#...
# Swarm: active
#  NodeID: i05ivyhuaas9e19xr1hlmyjm9
#  Is Manager: true
#  ClusterID: jqc1n0nhk1ctl77xz2euadspw
#  Managers: 1
#  Nodes: 1
#  Default Address Pool: 10.0.0.0/8  
#  SubnetSize: 24
#  Data Path Port: 4789
#  Orchestration:
#   Task History Retention Limit: 5
#  Raft:
#   Snapshot Interval: 10000
#   Number of Old Snapshots to Retain: 0
#   Heartbeat Tick: 1
#   Election Tick: 10
#  Dispatcher:
#   Heartbeat Period: 5 seconds

```

Try to see how many nodes are available.

```shell
docker node ls
#ID                            HOSTNAME                     STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
#i05ivyhuaas9e19xr1hlmyjm9 *   sparks-docker-admin          Ready     Active         Leader           20.10.13
```