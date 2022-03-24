We are going to create a container using tmpfs for fast filesystem storage.


```shell
# Map /tmpvol to a tmpfs partition, in memory only
docker run -d -ti --mount type=tmpfs,target=/tmpvol --name ctn1 python:3.7-alpine

# Execute commands and see the content change
docker run -d -ti --mount type=tmpfs,target=/tmpvol --name ctn1 python:3.7-alpine
#fe73f5941f616b4bc1137b170969273e0feb6c035d1f86d0652842b76c89ef05
docker volume ls
#DRIVER    VOLUME NAME
#local     newvol
docker run -d -ti --volumes-from ctn1 --name ctn2 python:3.7-alpine
#Unable to find image 'python:3.7-alpine' locally
#3.7-alpine: Pulling from library/python
```
