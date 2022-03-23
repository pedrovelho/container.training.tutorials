Assuming that you already have an image with all the python3 dependencies installed. You should just run
a new container now mapping the port 8080 from the container to the VM network interface.

```shell
# Create a new-container using the healthz image, now use --publish/-p
docker run -d --name healthz --publish 80:8080 --volume $HOME/healthz.py:/root/healthz.py ubuntu:healthz python3 /root/healthz.py

# Now you can try curl on the VM port 80
curl -v http://localhost/healthz
```

