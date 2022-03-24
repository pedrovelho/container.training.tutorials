Now that you have the credentials to work with dockerhub, let's store your images.

```shell
# If you try to push your image with the current tag your access will be denied by the registry
docker push alpine:healthz-optimized 
#The push refers to repository [docker.io/library/alpine]
#c327799c1e35: Preparing 
#c0b374dd81e1: Preparing 
#0fcb8cee59c1: Preparing 
#459cddbd4284: Preparing 
#7ced7bd0d279: Preparing 
#f57e81d89e60: Waiting 
#8d3ac3489996: Waiting 
#denied: requested access to the resource is denied

# You are actually only allowed to add images to your user, so you need to create a tag using 
# the syntax <dockerhub_username>/<image_name>:<image_tag>
docker tag alpine:healthz-optimized letrololo/alpine:healthz-optimized
docker images
#REPOSITORY         TAG                 IMAGE ID       CREATED        SIZE
#letrololo/alpine   healthz-optimized   d0e47cc4f819   20 hours ago   55.8MB

# Now you are allowed to push the image.
docker push letrololo/alpine:healthz-optimized 
#The push refers to repository [docker.io/letrololo/alpine]
#c327799c1e35: Pushed 
#c0b374dd81e1: Pushed 
#0fcb8cee59c1: Pushed 
#459cddbd4284: Pushed 
#7ced7bd0d279: Pushed 
#f57e81d89e60: Pushed 
#8d3ac3489996: Mounted from library/alpine 
#healthz-optimized: digest: sha256:ea8d5aebd15f72b693cccd48f509a9831612cc4a627854b340c0cbb960604f8b size: 1786
```

Once the image was pushed correctly you can check it on your dockerhub repositories.

![dockerhub image](./img/04-04-imageupload.png "dockerhub with the alpine:healthz-optimized image")


Now you can delete the local generated image and add it back again.

```shell
# Delete all containers and docker images
docker rm -f $(docker ps -aq)
docker rmi -f $(docker images -qa)

# Create a container using the dockerhub image
docker run -d --name healthz-alpine-opt --publish 80:8080 letrololo/alpine:healthz-optimized 
#Unable to find image 'letrololo/alpine:healthz-optimized' locally
#healthz-optimized: Pulling from letrololo/alpine
#59bf1c3509f3: Pull complete 
#07a400e93df3: Pull complete 
#4519a8e3082b: Pull complete 
#03a8252a96d7: Pull complete 
#b05058be7caa: Pull complete 
#c2396b4cbb67: Pull complete 
#d129ae9e07d4: Pull complete 
#Digest: sha256:ea8d5aebd15f72b693cccd48f509a9831612cc4a627854b340c0cbb960604f8b
#Status: Downloaded newer image for letrololo/alpine:healthz-optimized
#51a5d41e3cb32f97392401c42f18bad390d729d8332a249a45da1ab22e566d14

# Check your container is running and reponds to http get
docker ps 
#CONTAINER ID   IMAGE                                COMMAND                  CREATED          STATUS         PORTS                                   NAMES
#51a5d41e3cb3   letrololo/alpine:healthz-optimized   "/usr/local/bin/pyth…"   14 seconds ago   Up 9 seconds   0.0.0.0:80->8080/tcp, :::80->8080/tcp   healthz-alpine-opt
curl -v http://localhost/healthz
```

