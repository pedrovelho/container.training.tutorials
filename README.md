# sparks-docker-3d

Project to hold docker lecture for Sparks, final client is Renault Labs at Sophia-Antipolis.

## Resources

* [Docker official documentation](https://docs.docker.com/get-started/)
* [Github container-training free course by Jérôme Petazzoni](https://github.com/jpetazzo/container.training)
* [freeCodeCamp - The Docker Handbook 2021 Edition](https://www.freecodecamp.org/news/the-docker-handbook/)
* [The Docker Book](http://lsi.vc.ehu.es/pablogn/docencia/manuales/The%20Docker%20Book.pdf)

## VMs

Azure VMs, 1 vcpu, 500 MB RAM

## Plan des cours

### 1er journée (23/03/2022)

#### Théorie

* Intrduction
    * Motivation
        * Portability
        * Reproductibility
        * Security (sandboxing)
        * Automation
        * Flexibility
    * Historic
        * Virtualization
        * Hypervisor methods
        * Container vs Hypervisor
    * Concepts
        * Docker image
        * Docker registry
        * Docker container
        * service (if swarm mode)

#### Pratique

[01-install_docker](./tutorials/01-install_docker/README.md)

#### Théorie

* Docker architecture
    * docker flavors
        * Enterprise Edition : 1 day support included
        * Community Edition : free version
    * docker daemon
    * docker CLI
        * ps
        * images
        * run

#### Pratique

[02-docker_basics](./tutorials/02-docker_basics/README.md)

#### Théorie

* Basic of containers
    * Volumes
    * Port mapping
    * Images
    * Registry
        * dockerhub
        * local registry

#### Pratique

[03-docker_images](./tutorials/03-docker_images/README.md)

### 2eme journée (24/03/2022)

#### Theorie

* Building custom containers
    * Dockerfile
        * WORKDIR
        * FROM
        * COPY
        * RUN
        * CMD / ENTRYPOINT
* docker build
    * local registry
    * cleanup, docker system prune

#### Pratique

[04-docker_build](./tutorials/04-docker_build/README.md)

### Theorie

* Docker volumes
  * types of volumes
  * create a volume
  * backup volume content
  * remove volume
  * restore volume backup

#### Pratique

[05-docker_volumes](./tutorials/05-docker_volumes/README.md)

#### Theorie

* docker network
  * types
  * associate networks to containers
  * create/remove networks
  * connect/disconnect networks
  * name resolution
  * overlay network
  * plugins

#### Pratique

[06-docker_network](./tutorials/06-docker_network/README.md)

#### Theorie

* docker-compose
  * declarative syntax
  * yaml syntax
    * environment variables
    * publish ports
  * define multiple services/containers
  * configuration

#### Pratique

[07-docker-compose](./tutorials/07-docker-compose/README.md)

### 3eme journée (25/03/2022)

### Theorie

* Docker Swarm
  * Swarm mode
  * services
  * stack
  * secrets
  * load balancing
  * overlay network
  * troubleshooting

#### Pratique

[08-docker_swarm](./tutorials/08-docker-swarm/README.md)

### Demo

* CI/CD with docker
  * test environment (ryax_runner)
  * push on dedicated registry
* Kubernetes
  * deployment
  * pods
  * containers

