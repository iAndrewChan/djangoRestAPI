Project is based on the REST API with Python & Django udemy course django-python-advanced

Covering the following REST API topics:
...

## Dockerfile

Run docker image
- This is where I will try and create the files, as if was the environment I am developing with.

Run the docker image with bash to get the requirements.txt modules
```bash
docker run -it djangorest sh
```

Able to create our project and place the files in our host directory, so that we don't need a Python installed on our host machine.
```bash
docker-compose run app sh -c "django-admin startproject app ."
```

## CI with Travis CI

