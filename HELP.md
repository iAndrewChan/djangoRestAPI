## Dockerfile and Docker compose

### creating the project
Run docker image
- This is where I will try and create the files, as if was the environment I am developing with.

Run the docker image with bash to get the requirements.txt modules

```bash
docker run -it djangorest sh
# or 
docker-compose run app sh
```

Able to create our project and place the files in our host directory, so that we don't need a Python installed on our host machine.
```bash
docker-compose run app sh -c "django-admin startproject app ."
```

Run the django server
```bash
docker-compose up
```

### post-install docker and docker-compose

```bash
systemctl start docker
systemctl enable docker
sudo usermod -aG docker $USER # add user to have docker group to be able to run docker commands
groups $USER # to see docker has been added to user groups
reboot
```

### running shell commands in docker

```bash
docker run -it djangorest sh -c "pytest"
```

### running shell commands in docker-compose
Running black on app dir

```bash
docker-compose run app sh -c "black app"
docker-compose run app sh -c "pytest"
```

### Building docker-compose image without cache

```bash
docker-compose build --no-cache
```
### Different paths for docker builds and docker compose
https://stackoverflow.com/questions/63729349/why-different-copy-paths-between-docker-build-and-docker-compose-builds

### Named volume not updating from source file changes

The volume is to be able to make changes in the container and persist those changes on the host.

Changes made made in the Dockerfile that is in the same directory as the path of the mounted volume will not change data contained in the volume.

It looks like you're trying to use docker-compose with a named volume mount and a Dockerfile to modify the contents of that location. This won't work because the Dockerfile is creating an image. The docker-compose is defining the running container that runs on top of that image. You won't be able to modify the volume within the image creation since that volume is only mounted after the image is created an you run the container.

https://stackoverflow.com/questions/38441158/docker-named-volume-not-updating

#### remove the volume all together if we want the contents of the image
Solution: remove the volume all together where I want the contents of the image

#### volume reflects the files in the host

We are able to move the files into the directory that has been attached to the docker volume

