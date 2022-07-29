# SpeedPyCom Starter Template

## Quickstart

This is the starter template for SpeedPyCom and you can edit any file you want.

To update the SpeedPyCom you need to update the requirements.txt file to have the most recent speedpycom package.

https://pypi.org/project/speedpycom/

### Get the template and start work

For local development you should have Docker instance running locally. Read more about docker-compose.yml down the
document.

```bash
curl -sSL https://gitlab.com/speedpycom/speedpycom-start/-/archive/main/speedpycom-start-main.zip > speedpycom-start-main.zip
unzip speedpycom-start-main.zip


mv speedpycom-start-main myproject
cd myproject
cp start.env .env

```


Apply migrations with:

```bash
docker-compose run web python manage.py migrate
```

Create a superuser account:

```bash
docker-compose run web python manage.py makesuperuser
```

The output of the last command will display the login and password for the admin user that was created, like this:

```
admin user not found, creating one
===================================
A superuser was created with email admin@example.com and password xLV9i9D7p8bm
===================================
```

Install tailwind dependencies and build it:

```bash
docker-compose run web python manage.py tailwind install
docker-compose run web python manage.py tailwind build
```

Run the project with:

```bash
docker-compose up
```


Open [http://0.0.0.0:8060/admin/](http://0.0.0.0:8060/admin/) and login with these credentials.

## Docker-Compose.yml for local development

This template implies using Docker for local development.

If you don't have Docker installed go
to [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop) and follow
installation instructions for your OS.

`docker-compose.yml` file has a number of services defined to run the project.

To reduce the initial resource usage on your machine only few of them are uncommented and will be used:

- `redis`
- `db`
- `web`

If you need Celery - uncomment all lines for the `celery` service.

Same way, if you need Celery Scheduler – uncomment `celery-beat` service.

Flower (celery monitoring) is also included, uncomment `flower` service in order to have it running.

For the purpose of using less resource of your machine Redis is used for Celery broker by default.
You can easily switch to using RabbitMQ by uncommenting `rabbitmq` service and `rabbitmq` in all services' `links`
and `depends_on` sections. Then in `.env` change the broker setting to this: `CELERY_BROKER_URL=amqp://speedpycom:speedpycom@rabbitmq/speedpycom` and `docker-compose restart` so the new settings are
applied.

## Dockerfile

Docker file includes both Python and Node so you can have JS compilers, minifiers and use `django-tailwind` that is included into this template.


## Deployment

In order to deploy the project on [https://Appliku.com](https://Appliku.com) we have included the `Procfile` with commands needed to run your project.


## User model

Project template comes with a custom user model in the app `usermodel`.

## Tailwind

Run `docker-compose run web python manage.py tailwind install` to install node dependencies to run tailwind.

