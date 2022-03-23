
Create a container that wait for user input on bash.

```shell
# Create a container, you can use -n for --name, and -i for --interactive
docker container create --name new-container --interactive ubuntu bash
#df202644ebae55674243b12aa1827087f34542db64d82611ddef5c61ce6074b5

# Check the container was created
docker ps -a
#CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS    PORTS     NAMES
#df202644ebae   ubuntu    "bash"    6 seconds ago   Created             new-container

# Start the container
docker start new-container

# Check container status is now running
# Up 3 seconds means running for 3 seconds
docker ps
#CONTAINER ID   IMAGE     COMMAND   CREATED              STATUS         PORTS     NAMES
#df202644ebae   ubuntu    "bash"    About a minute ago   Up 3 seconds             new-container

# You can execute commands on the container with docker exec
# For instance, try ps on the container to see the only process running is bash and the ps issued command
docker exec new-container ps
#    PID TTY          TIME CMD
#      1 ?        00:00:00 bash
#      7 ?        00:00:00 ps


# Drop a shell inside the container, with -t short for --tty option the input/output is redirected from the
# container terminal, interactive mode is needed to wait for commands on the dropped shell
docker exec -ti new-container bash # To come back simply use exit

# Stop a running container
docker stop new-container
docker ps -a
#CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS                       PORTS     NAMES
#df202644ebae   ubuntu    "bash"    4 minutes ago   Exited (137) 4 seconds ago             new-container


# You can launch again a stopped container
docker container start new-container
docker ps
#CONTAINER ID   IMAGE     COMMAND   CREATED              STATUS         PORTS     NAMES
#df202644ebae   ubuntu    "bash"    About a minute ago   Up 9 seconds             new-container

# To remove a container you need to stop it first, or you can force removal with -f/--force option
docker rm -f new-container

# Alternativlely, use docker run to create and start the container in a single line
docker run -i -d --name new-container ubuntu bash
# The last will run a new container interactively -i in detached mode -d
# this options will make the container run the bash process indefinitely as before


```

