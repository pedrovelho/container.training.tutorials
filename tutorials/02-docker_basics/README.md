# Docker Basics

On the previous tutorial you managed to get access to a VM and get docker installed and running. From now on we assume
that you are already using the provided VM and that docker is installed correctly. If you need help just ask.

Through this tutorial you will:

* Learn how to execute basic docker commands:
    * create containers
    * list running containers
    * drop a shell on running container
    * find dangling containers
    * remove containers

## Create containers

In the previous exercise we used the `docker run` command to create and launch a container. However, the container
life-cycle include many stages. In a matter of fact, it is possible to create a container as is without running any
process on it. For instance, to create a container without running any command you can use:

```sh
docker container create -t --name my-container ubuntu
```

Example output:

```
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
7c3b88808835: Pull complete
Digest: sha256:8ae9bafbb64f63a50caab98fd3a5e37b3eb837a3e0780b78e5218e63193961f9
Status: Downloaded newer image for ubuntu:latest
8dfc3436d5b929f522f41d57e26c5c3a70e1a892e5b1bacfbfbcead68db6e81f
```

The command container create has mandatory parameter image, `ubuntu` above. Container
parameter `--name <container-name>` is optional, when omitted docker will pick a random name. The `-t` parameter is a
short for `--tty` this will allow the container to sit waiting for user input, making it possible to run indefinitely.
This option prevents this container to immediately exit after started.

Upon success create command return the full container id, this means all image layers are pulled (`downloaded`) from
the remote docker registry if not yet locally available and the container is created but not started. This slightly
differs from `docker run` that will also start the container. From now on you can either reference a container by its
name or id, docker CLI will handle both seamlessly.

To interact with the docker daemon and see the containers and their status you can use `docker ps`
or `docker container list`, however only currently running containers appear by default. To list all containers
use `docker ps -a` or `docker container ls -a` where the `-a` stands for all containers (even stopped or finished ones).

```sh
docker ps -a
```

Example output:

```
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS    PORTS     NAMES
8dfc3436d5b9   ubuntu    "bash"    5 minutes ago   Created             my-container
```

## **Exercise**: Figure out how many containers are currently there

- Run `docker ps -a`, what do you see? How many containers? Are their status the same?
- Run `docker ps`. Do you see less containers? Why?

> See the [solution](./answer/02-01-containers.md)

## Start container

Continuing the life-cycle of a container we might need to run some program inside the container. The first step on that
direction would be to start the container, once the container is running you ideally will want to drop a shell prompt on
the container to start working. If you try to execute commands on a stopped or exited container an error will occur. Go
ahead and start your container:

```sh
docker container start my-container
```

Now you can check it is running by using `docker ps` again. If your container is running start a shell on the container
by running `bash` with the command below.

```sh
docker exec -ti my-container bash
```


## **Exercise**: Install a package on a container

Try to install `cowsay` package inside a container.
```shell
apt-get install cowsay
```
- Is the package installed correctly? (tip: `/usr/games/cowsay`)
- Can you execute it correctly?
- Can you execute that command outside the container?

Now try to create a new container using the same `ubuntu` image.
- Does this new container contain the command cowsay installed? Why?

> See the [solution](./answer/02-02-cowsay.md)


## Container safe environment

One of the main initial motivations for containers and virtual machines was to provide a safe environment where
the user has root access but no harm on that environment can be extended to the host itself. 
So inside a container you can run commands safely and experiment fault scenarios: what if... a file is corrupted,
a process unexpectedly shuts down, network connection drop and restart. 

For instance, one thing that completely wracks a linux system is to remove the `/lib` directory. 
Try out for instance to remove your `/lib` directory inside the
container. Caution to not do it on your VM but within a container. You will probably kill the container but this is not
a problem, you can just create a new one from the same image and drop a shell again.


## **Exercise**: Wrack a container, stop and remove containers


Delete `/lib` (**WARNING within the container**) you probably can't execute anything anymore, bash, ls, etc all gone. But
with `docker ps -a` you should still see the faulty container running.

- Stop a faulty container using `docker stop my-container` and start again, does it solve the issue?
- Try to create a new container using the same `ubuntu` image, does this new container still has `/lib`?
- Now try to remove the wracked container.
- What clever ways can you come up with to fix this container?

> See the [solution](./answer/02-03-lib.md)
