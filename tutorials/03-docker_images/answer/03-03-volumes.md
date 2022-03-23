First create a new image with your changes and then run that new image with option --volume/-v
to map the file inside the container.

```shell
# Commit your changes to the container
docker commit new-container ubuntu:healthz
#sha256:4a2cc691d57518c4da047aada404f3aa5ca06f257a06d91a3b57a9830ecb3b4c
docker images -a
#REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
#ubuntu       healthz   4a2cc691d575   33 seconds ago   446MB
#ubuntu       cowsay    7a6a50053941   2 days ago       153MB
#ubuntu       latest    2b4cba85892a   10 days ago      72.8MB

# Create a new-container using the healthz image, now use --volume/-v optiion to map the healthz.py file
docker run -d --name healthz --volume $HOME/healthz.py:/root/healthz.py ubuntu:healthz python3 /root/healthz.py

# Check the service is running
docker exec -t healthz curl -v http://localhost:8080/healthz
```
