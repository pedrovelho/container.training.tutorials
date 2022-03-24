
We can check the image size using.

```shell
docker images
#REPOSITORY       TAG       IMAGE ID       CREATED         SIZE
#ubuntu-healthz   latest    2686f674b622   7 minutes ago   446MB
#ubuntu           latest    ff0fea8310f3   2 days ago      72.8MB
```

The base image `ubuntu` and result image `ubuntu-healthz` have a huge size difference, 446MB and 73MB.
In practice a main problem here is that we are building the dependencies and having all the build
tool-chain available on the final image. Moreover, we can check that we have many layers with dive. Every
Dockerfile command generates a new layer and hence increase the complexity of maintaining the image.


To start getting a reduced image we can try to improve our base image. Inspecting in docker hub we have
a tag with pre-installed [python:3.7-alpine](https://hub.docker.com/layers/python/library/python/3.7-alpine/images/sha256-6d5312ecd722ad058529c2e2dce30cf3100756ba2b632c878d78460ce6a82272?context=explore). 
has only 16MB.

```shell
FROM python:3.7-alpine

RUN pip install aiohttp

CMD /app
COPY healthz.py /app/healthz.py

ENTRYPOINT [ "/usr/local/bin/python3", "/app/healthz.py" ]
```

We can build again using a different docker file.

```shell
docker build -t healthz-python . -f Dockerfile.alpine
#Step 5/5 : ENTRYPOINT [ "/usr/local/bin/python3", "/app/healthz.py" ]
# ---> Running in 58fccabd9126
#Removing intermediate container 58fccabd9126
# ---> 2cbab9f280bd
#Successfully built 2cbab9f280bd
#Successfully tagged healthz-python:latest

# See image size
docker images
#REPOSITORY       TAG          IMAGE ID       CREATED          SIZE
#healthz-python   latest       2cbab9f280bd   9 minutes ago    64.3MB

# Check the image is working
docker run -d -p 80:8080 --name healthz healthz-python
#c3c5ea010983823cf47863cd56ab9a6d428b155b3c6560f68831bf8afbd30f8a
curl http://localhost/healthz
```

The final result is 64.3 MB way less than the ubuntu based image.
To improve the image even more we can use a Dockerfile with the build pattern
so that we avoid temporary, cached, and configuration files on the final image.

```shell
FROM python:3.7-alpine AS base
FROM base AS builder
RUN mkdir /install
RUN pip3 install --prefix=/install aiohttp

FROM base
COPY --from=builder /install /usr/local
COPY healthz.py /app/healthz.py
ENTRYPOINT [ "python3", "/app/healthz.py" ]
```

We build and test this image using a new Dockerifle.

```shell
docker build -t healthz-python-opt . -f Dockerfile.alpine-optimized
docker run -d -p 80:8080 --name healthz healthz-python-opt
#df4862f0ffedea67b1dcc0d4cbf26cb69d6cd2e75ae69fedbfad237fa42c672b
curl http://localhost/healthz


# Compare the images
docker images
#healthz-python-opt   latest       cf1d903cd6b7   About a minute ago   55MB
#healthz-python       latest       ff8a39341da8   3 minutes ago        64.3MB
#ubuntu-healthz       latest       2686f674b622   37 minutes ago       446MB

```

After build the new optimized image has 55MB, about 20% less disk space.

