We are going to create a volume and link to 2 containers.


```shell
# Create a volume
docker volume create myol

# List volumes
docker volume ls
#DRIVER    VOLUME NAME
#local     myvol

# Inspect myvol, type is local by default
docker volume inspect myvol
#[
#    {
#        "CreatedAt": "2022-03-20T09:57:40Z",
#        "Driver": "local",
#        "Labels": {},
#        "Mountpoint": "/var/lib/docker/volumes/myvol/_data",
#        "Name": "myvol",
#        "Options": {},
#        "Scope": "local"
#    }
#]


# Now spin 1 container that uses myvol
docker run -d -ti --mount source=myvol,target=/myvol --name ctn1 python:3.7-alpine
#383aa636413f91bfbded79631b75142f728a6fc8822ac3cc89e6783bcc4940cc

# We can see that the volume was attached succesfully on the target, and that we can create 
# files as a regular directory
docker exec ctn1 ls /myvol
docker exec ctn1 touch /myvol/file.txt
docker exec ctn1 ls /myvol
#file.txt

# Now let's create a secondary container with same volumes as ctn1, we will use the option
# --volumes-from
docker run -d -ti --volumes-from ctn1 --name ctn2 python:3.7-alpine


# We can see /myvol is there with the shared files.
docker exec ctn2 ls /myvol
#file.txt
```

