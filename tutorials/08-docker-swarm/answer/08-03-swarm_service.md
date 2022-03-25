Lets create a simple service.

```shell
# Create service
docker service create --name pingpong alpine ping 8.8.8.8
#wvy1ggu14eat49qha7xiwmvpj
#overall progress: 1 out of 1 tasks 
#1/1: running   [==================================================>] 
#verify: Service converged 

#In which node is the project running?
docker service ps pingpong
#ID             NAME         IMAGE           NODE                  DESIRED STATE   CURRENT STATE            ERROR     PORTS
#mar4ss89mwqx   pingpong.1   alpine:latest   sparks-docker-admin   Running         Running 36 seconds ago 

#Can you access the service logs?
docker service logs -f -n 4 pingpong
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=377 ttl=114 time=2.646 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=378 ttl=114 time=2.111 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=379 ttl=114 time=4.388 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=380 ttl=114 time=2.775 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=381 ttl=114 time=2.331 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=382 ttl=114 time=1.689 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=383 ttl=114 time=1.646 ms

# Create 4 replicas
docker service update pingpong --replicas 4
#pingpong
#overall progress: 4 out of 4 tasks 
#1/4: running   [==================================================>] 
#2/4: running   [==================================================>] 
#3/4: running   [==================================================>] 
#4/4: running   [==================================================>] 
#verify: Service converged 

# Check the replicas' node, we see 2 running on admin and 2 on worker
docker service ps pingpong
#ID             NAME         IMAGE           NODE                         DESIRED STATE   CURRENT STATE            ERROR     PORTS
#mar4ss89mwqx   pingpong.1   alpine:latest   sparks-docker-admin          Running         Running 9 minutes ago              
#c8kaouqavkj1   pingpong.2   alpine:latest   sparks-docker-admin          Running         Running 38 seconds ago             
#v39id2z53jde   pingpong.3   alpine:latest   sparks-docker-admin-worker   Running         Running 35 seconds ago             
#m7kzy0sxd8q8   pingpong.4   alpine:latest   sparks-docker-admin-worker   Running         Running 35 seconds ago             


# Logs show results for the many containers running interchangeably
docker service logs -f pingpong
#pingpong.3.v39id2z53jde@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=74 ttl=114 time=2.824 ms
#pingpong.3.v39id2z53jde@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=79 ttl=114 time=3.091 ms
#pingpong.3.v39id2z53jde@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=80 ttl=114 time=2.833 ms
#pingpong.3.v39id2z53jde@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=81 ttl=114 time=2.723 ms
#pingpong.4.m7kzy0sxd8q8@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=75 ttl=114 time=2.751 ms
#pingpong.4.m7kzy0sxd8q8@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=76 ttl=114 time=2.795 ms
#pingpong.4.m7kzy0sxd8q8@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=77 ttl=114 time=3.402 ms
#pingpong.4.m7kzy0sxd8q8@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=78 ttl=114 time=3.145 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=609 ttl=114 time=2.400 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=610 ttl=114 time=1.726 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=611 ttl=114 time=5.400 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=612 ttl=114 time=2.269 ms
#pingpong.2.c8kaouqavkj1@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=81 ttl=114 time=3.220 ms
#pingpong.2.c8kaouqavkj1@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=82 ttl=114 time=1.588 ms
#pingpong.2.c8kaouqavkj1@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=83 ttl=114 time=1.445 ms
#pingpong.2.c8kaouqavkj1@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=84 ttl=114 time=1.804 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=613 ttl=114 time=1.636 ms
#pingpong.2.c8kaouqavkj1@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=85 ttl=114 time=1.649 ms
#pingpong.3.v39id2z53jde@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=82 ttl=114 time=2.772 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=614 ttl=114 time=2.032 ms
#pingpong.2.c8kaouqavkj1@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=86 ttl=114 time=1.941 ms
#pingpong.3.v39id2z53jde@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=83 ttl=114 time=3.070 ms
#pingpong.1.mar4ss89mwqx@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=615 ttl=114 time=1.736 ms
#pingpong.2.c8kaouqavkj1@sparks-docker-admin    | 64 bytes from 8.8.8.8: seq=87 ttl=114 time=1.569 ms
#pingpong.4.m7kzy0sxd8q8@sparks-docker-admin-worker    | 64 bytes from 8.8.8.8: seq=84 ttl=114 time=2.980 ms
#^C


```






