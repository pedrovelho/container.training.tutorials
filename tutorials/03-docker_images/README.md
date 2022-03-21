# Handle images and layers

On the previous tutorial we saw that we can modify the content of one container, this will persist even if we
stop/restart the same container. However, we also observed that creating a new container will not include that
modification, this is indeed a designed feature. Docker run containers based on images. Containers are instances of that
image and hence a modification to the content of a container does not affect its image, unless we want it too.

In docker a registry is a repository of images, for instance [hello-world](https://hub.docker.com/_/hello-world)
and [ubuntu](https://hub.docker.com/_/ubuntu) are both official images that were downloaded from the internet when we
requested to run containers of these images. A series of images are already available from the docker-hub registry
some are officially supported but anyone can create their own images (more on that later).

# List images

Once you pull an image from the registry, it is locally available, you can list the locally available images by
running `docker images -a`.

# Inspect layers

To inspect the layers of an image we are going to use the dive tool. To install it simply run:

```shell
wget https://github.com/wagoodman/dive/releases/download/v0.9.2/dive_0.9.2_linux_amd64.deb
sudo apt install ./dive_0.9.2_linux_amd64.deb
```

Now you can use dive to check the layers you have on a given image.

```shell
dive ubuntu:latest
```

After that you can check that even if you did change your image, for instance running `apt-get install`,
it is still the original image from dockerhub. That is why when you create a new container from this image,
all changes you might have will be lost.


# Modify an existing docker image

To change an image there are 2 main approaches:
- Create a new image using `docker build` command;
- Add changes to a container and create a new image with `docker commit`. 


## **Exercise**: Create a docker image with the cowsay package pre-installed

Install cowsay or any other package on your container. Now commit that change using 
`docker commit`, try `docker commit --help` to check the options available.

- Create an `ubuntu` container
- Now add the `cowsay` program by running `apt-get install cowsay`
- The program should appear in `/usr/games/cowsay`, try it out `/usr/games/cowsay hello`
- Now commit this changes using `docker commit ubuntu:cowsay`
- Check that the new images exists locally with name and tag `ubuntu:cowsay`
- Run cowsay from a new container image `docker run ubuntu:cowsay /usr/games/cowsay hello mom`

Use dive to inspect the image.

- What is the size of the new image? Is it the same of the base `ubuntu:latest` image?
- How many layer the new image has?
- Can we come up with a clever way to compress this image?

> See the [solution](./answer/03-01-cowsay.md)


## **Exercise**: Run a simple http server as a docker container 

Now let's say we want to add a http service to the container, a simple server that answer 200 on port
8080. This is a very simple health check and in python we can easily do it with the following script:

```python
from aiohttp import web

async def healthz(request):
    print("Called healthz endpoint")
    return web.Response()

app = web.Application()
app.add_routes([web.get('/healthz', healthz, allow_head=False)])
web.run_app(app) # loop until interrupted
```

Use `docker cp` or map a volume to copy the file inside the container. You will need to install try 
`apt-get install python3 curl`. Also install the web application package, `pip install aiohttp`. 
Now you should be able to run the script above on the container. To test it try inside the container:

```shell
curl http://localhost:8080/healthz
```

> See the [solution](./answer/03-02-healthz.md)

## **Exercise**: Working volumes

Create a new container from scratch but now use a volume to map the healthz.py file inside the container.

> See the [solution](./answer/03-03-volumes.md)

## **Exercise**: Publish TCP port

Create a new container and now expose the TCP port so that curl on the VM http://localhost/healthz will redirect
to the correct container and port.

> See the [solution](./answer/03-04-port_mapping.md)
