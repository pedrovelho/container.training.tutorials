
#  Docker Swarm

Now you can have access to a second node <yournodename>-worker. To connect use the same private-key. Once you are 
connected do the exercises below.

## **Exercise**: Swarm init

Init a swarm manager on the main VM.

> See the [solution](answer/08-01-swarm_init.md)

## **Exercise**: Add one worker

Now add a worker on the second node. Can you see the node list? Are all nodes available?

> See the [solution](answer/08-02-swarm_worker.md)

## **Exercise**: Create the first service.

Create a simple service. In which node is the service running? How many containers are running?
Can you replicate containers for that service? Can you access the service logs?

> See the [solution](answer/08-03-swarm_service.md)

## **Exercise**: Modify docker-compose.yml of the rest-server

Now deploy the previous exercise example as 2 services, one is redis and another is the rest-server
itself. What changes do you need so the docker-compose.yaml work on swarm.

> See the [solution](answer/08-04-docker-compose_services.md)

## **Exercise**: Create a secret to store redis password

Using the redis password on the docker-compose file is a security breach. How can you manage that
value using a docker secret?

> See the [solution](answer/08-05-secret.md)





