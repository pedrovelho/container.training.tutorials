From the previous exercise volume we have already at least one file inside.
Now we are going to backup the volume.

```shell
# Stop all containers
docker rm -f $(docker ps -aq)
#b58fc855c6a9
#383aa636413f

# Now run a container to execute a tar command for backing up
# Need to also map the /backup folder on the container to where the output is generated
docker run -ti --mount source=myvol,target=/myvol --mount type=bind,src=$HOME,dst=/backup --name ctn1 python:3.7-alpine tar cvf /backup/backup.tar /myvol
# The resulting file appears on the home directory
ls -la backup.tar
backup.tar

# Now we can remove the original volume and create a new volume to restore the content
docker rm -f $(docker ps -aq)
#ddcc5e21ece5
docker volume rm myvol
#myvol
docker volume ls
#DRIVER    VOLUME NAME
docker volume create newvol
#newvol

# Finally we restore the content and verify it is all there
docker run -ti --mount source=newvol,target=/myvol --mount type=bind,src=$HOME/backup.tar,dst=/backup.tar --name ctn1 python:3.7-alpine sh -c "cd /myvol && tar xvf /backup.tar --strip 1"
#myvol/
#myvol/file.txt

docker run -d -ti --mount source=newvol,target=/myvol --name ctn2 python:3.7-alpine
docker exec ctn2 ls /myvol
#file.txt
```

