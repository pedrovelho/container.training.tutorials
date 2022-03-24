
```shell
echo "something" > $HOME/shared_file.txt

docker run -d -ti -v $HOME/shared_file.txt:/shared.txt --name ctn1 python:3.7-alpine
#b19e380530184c9bd93f3f59ccea94946b59b322951f696ac2e751d40f547a98

docker ps -a
#CONTAINER ID   IMAGE               COMMAND     CREATED         STATUS         PORTS     NAMES
#b19e38053018   python:3.7-alpine   "python3"   3 seconds ago   Up 2 seconds             ctn1

docker run -d -ti -v $HOME/shared_file.txt:/shared.txt --name ctn2 python:3.7-alpine
#be8e401f2e79f225bd7dcb0945ea9daff5635182b187d06c9f7c43cfb97e7c3c

docker ps -a
CONTAINER ID   IMAGE               COMMAND     CREATED              STATUS              PORTS     NAMES
be8e401f2e79   python:3.7-alpine   "python3"   About a minute ago   Up About a minute             ctn2
b19e38053018   python:3.7-alpine   "python3"   2 minutes ago        Up 2 minutes                  ctn1


docker exec ctn2 sh -c 'echo "changecontent" > /shared.txt' 
docker exec ctn2 cat /shared.txt
#changecontent
docker exec ctn1 cat /shared.txt
#changecontent
docker exec ctn1 sh -c 'echo "changecontentAGAIN" > /shared.txt' 
docker exec ctn1 cat /shared.txt
#changecontentAGAIN
docker exec ctn2 cat /shared.txt
#changecontentAGAIN
cat shared_file.txt 
#changecontentAGAIN
echo "hello" > shared_file.txt 
docker exec ctn2 cat /shared.txt
#hello
```

As we can see from the commands above the file is shared between the host and the 2 containers. Any change on the 
file is seen on the containers and the host. Also we can see that anyone can change the file content as well.