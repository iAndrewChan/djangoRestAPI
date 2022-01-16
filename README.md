Project is based on the REST API with Python & Django udemy course django-python-advanced

Covering the following REST API topics:
...

## Getting started

Running locally with docker-compose:

```bash
docker-compose up -d
```

Go to the url:
`localhost:8000`

## Getting started with development

```bash
docker-compose run app sh # run container and start shell prompt
docker-compose run app sh -c "black app" # run container and execute the following shell command
docker-compose run app sh -c "pytest"
```

## CI with github actions