
#  Docker-compose

With docker compose you will be able to launch several containers that require a certain level of configuration to
work together in order to have a final running application. To start, first install `docker-compose` on your VM.

```shell
sudo apt-get install docker-compose
```

Now let's use a more complex application. You can find this application [here](rest-server).

## **Exercise**: Create an image for the application

Follow the instructions on the README file to create an image for the application.

> See the [solution](./answer/07-01-rest-server_img.md)

## **Exercise**: docker-compose

The application requires a redis instance to run. Redis is a simple file store already
available on dockerhub. Put the instructions of the README.md on a docker-compose.yaml file.
Test the service from within the container.

> See the [solution](./answer/07-02-docker-compose.md)




