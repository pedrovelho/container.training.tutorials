On the host you can commit this changes in a new docker image.

```shell
# List locally available images
docker images -a
#REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
#ubuntu       latest    2b4cba85892a   10 days ago   72.8MB


# Check that my-container is running
docker ps
#CONTAINER ID   IMAGE     COMMAND   CREATED      STATUS      PORTS     NAMES
#150c130b8751   ubuntu    "bash"    2 days ago   Up 2 days             my-container

# Check the differences between your my-container and its original image
docker diff my-container

# Add the change using docker commit
# Feel free to use options --author, --message, etc. 
docker commit my-container ubuntu:cowsay

# Now check the newly created image
docker images -a
#REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
#ubuntu       cowsay    7a6a50053941   2 days ago    153MB
#ubuntu       latest    2b4cba85892a   10 days ago   72.8MB

# Test that new containers have cowsay as expected
docker run ubuntu:cowsay /usr/games/cowsay hello mom
# ___________
#< hello mom >
# -----------
#        \   ^__^
#         \  (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||


# You can also verify that containers from the orignial image do not have cowsay installed
docker run ubuntu /usr/games/cowsay hello mom
#docker: Error response from daemon: failed to create shim: OCI runtime create failed: container_linux.go:380: starting container process caused: exec: "/usr/games/cowsay": stat /usr/games/cowsay: no such file or directory: unknown.
#ERRO[0003] error waiting for container: context canceled
```

As you can see a new images appears and this image has twice the size of its original image, we
will soon learn how to make a better management of the disk. On the dive program we can see
many more info for the new created image.

![dive to inspect a docker image](./img/03-01-cowsay_image.png "dive ubuntu:cowsay")
