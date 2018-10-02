Django test
=======================

Task
---------

Create a simple todo app with the functionality to create/list/update/delete. The todo's should be stored in the database and the rest is up to you.

Please don't spend more than 2 hours on this. On completion, please provide a link to the completed task on your github.


To run
---------
```bash
$ docker-compose build
$ docker-compose up
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
```

Once the docker container is working and running a separate terminal should be used to handle the management commands to migrate and create a super user.

Visit in a browser http://localhost:8000/admin and login with the superuser credentials you just created.
