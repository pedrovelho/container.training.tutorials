# sparks-docker-3d

Project to hold docker lecture for Sparks, final client is Renault Labs at Sophia-Antipolis.

## Resources

* [Docker official documentation](https://docs.docker.com/get-started/)
* [Github container-training free course by Jérôme Petazzoni](https://github.com/jpetazzo/container.training)
* [freeCodeCamp - The Docker Handbook 2021 Edition](https://www.freecodecamp.org/news/the-docker-handbook/)
* [The Docker Book](http://lsi.vc.ehu.es/pablogn/docencia/manuales/The%20Docker%20Book.pdf)

## VMs

Azure VMs, 1 vcpu, 1 GB RAM

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
* Virtualization vs containarization
* Historic
  * LXC
  * jails
* Docker echosystem
  * Docker CE vs Docker EE
  * Docker daemon
  * Docker CLI
* Install docker

#### Pratique

[01-install_docker](./tutorials/01-install_docker/README.md)

#### Théorie

* Containers
  * Life-cycle
  * Backgroud
  * Restarting and attaching
  * Naming and inspecting
  * Labels
  * Getting inside

#### Pratique

[02-docker_basics](./tutorials/02-docker_basics/README.md)

#### Théorie

* Docker images
  * Images, layers, and containers
  * Create image interactively
  * Backup/Restore
* Dockerhub and local registry

#### Pratique

[03-docker_images](./tutorials/03-docker_images/README.md)

### 2eme journée (24/03/2022)

#### Theorie

* Building custom images
  * Dockerfile
    * FROM
    * COPY
    * RUN
    * CMD / ENTRYPOINT
* How build cache works
* Reducing image size
  * Collapsing layers
  * Multi-stage builds
* Push images to dockerhub

#### Pratique

[04-docker_build](./tutorials/04-docker_build/README.md)

### Theorie

* Docker volumes
* Types of volumes
* Creating a volume
* Backup/restore content

#### Pratique

[05-docker_volumes](./tutorials/05-docker_volumes/README.md)

#### Theorie

* Docker network basics
  * Types
  * Associate networks to containers
* Creating/remove networks
* Connecting/disconnecting networks
* Name resolution
* Overlay network
* Plugins

#### Pratique

[06-docker_network](./tutorials/06-docker_network/README.md)

#### Theorie

* docker-compose
* Declarative syntax
* Syntax for yaml
* Declaring environment variables
* Publish ports
* Define multiple services/containers
* Configuration

#### Pratique

[07-docker-compose](./tutorials/07-docker-compose/README.md)

### 3eme journée (25/03/2022)

### Theorie

* Docker Swarm
  * Install a swarm
  * Manager and worker
* Services
* Stacks
* Overlay network
* Troubleshooting
* Secrets

#### Pratique

[08-docker_swarm](./tutorials/08-docker-swarm/README.md)

### Demo

* CI/CD with docker
* Test environment (ryax_runner)
* Push on dedicated registry
* Kubernetes
* Deployment
* Pods
* Containers

