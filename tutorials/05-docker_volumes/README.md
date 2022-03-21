# Working with volumes

We already worked with docker images. However, we do not yet handle an important subject:
How to make containers talk to each other. We can use the network for that, or we can also
use volumes creating a filesystem mount point that is shared among containers.

You can access besides the given slides the docker official documentation on volumes 
[here](https://docs.docker.com/storage/volumes/).

## **Exercise**: Shared file

Share a file among 2 containers. What happens when the file changes on one container?

> See the [solution](./answer/05-01-shared_file.md)

## **Exercise**: Create a volume

Create a volume and use it to share file among 2 containers. Create a file inside one container,
verify that the file also appears on the other container.

> See the [solution](./answer/05-02-volume.md)
    
## **Exercise**: Backup/Restore a volume

Stop the running containers, backup the volume, and delete it. Restore the volume
and start new containers, verify that the content of the volume is still available.

> See the [solution](./answer/05-03-volume_backup.md)

## **Exercise**: Mount tmpfs in a container.

Mount a tmpfs, in memory filesystem, on the container.

> See the [solution](./answer/05-04-volume_tmpfs.md)

