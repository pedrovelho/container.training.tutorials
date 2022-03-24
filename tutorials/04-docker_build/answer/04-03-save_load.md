To make a backup of your image you can use the save/load commands like below.

```shell
# Check the image name and tag you want to save
docker images
#REPOSITORY         TAG                 IMAGE ID       CREATED         SIZE
#alpine             healthz-optimized   286d601a4c5a   2 minutes ago   55.8MB

# Now let's make a backup for image alpine and tag healthz-optimized
# for convinience we put the output on file name healthz_optmized.tgz
docker save alpine:healthz-optimized > healthz_optmized.tgz

# Finally check the size of the backup image file
du -hs healthz_optmized.tgz 
#57M	healthz_optmized.tgz

# Check the file format as well
file healthz_optmized.tgz 
#healthz_optmized.tgz: POSIX tar archive


# So to get the image back from a backup with same name we first remove the image
docker rmi -f alpine:healthz-optimized 
# Untagged: alpine:healthz-optimized

# We can check the image is not there anymore
docker images
#REPOSITORY         TAG                 IMAGE ID       CREATED         SIZE

# Now let's restore the backup image with docker load
docker load < healthz_optmized.tgz 
#Loaded image: alpine:healthz-optimized

# Finally see that the image is back in place
docker images
#REPOSITORY         TAG                 IMAGE ID       CREATED         SIZE
#alpine             healthz-optimized   286d601a4c5a   4 minutes ago   55.8MB
```

