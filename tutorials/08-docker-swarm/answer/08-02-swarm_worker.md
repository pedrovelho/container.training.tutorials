Install docker on the other VM, follow the instruction on the official documentation,
or get the answer from the [first tutorial](../../01-install_docker/answer/01-01-install_docker.md).
Verify the installation as in [here](../../01-install_docker/answer/01-02-run_hello-world.md).


```shell
docker swarm join --token SWMTKN-1-5v8ourkgbb6r9pke6zmyek9ayj38tmfku8e4vlrjsgf25wxuyg-8vsmb51juwtvlw5mt7wk9npfw 172.17.0.6:2377
#This node joined a swarm as a worker.
```

Now we can see the nodes on the swarm changing, note that this command can only be issued on the swarm
manager. From now on we assume we are at the swarm manager.

```shell
docker node ls
#ID                            HOSTNAME                     STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
#i05ivyhuaas9e19xr1hlmyjm9 *   sparks-docker-admin          Ready     Active         Leader           20.10.13
#9mor95s51b0lb6l9b1n00gu09     sparks-docker-admin-worker   Ready     Active                          20.10.13
```
