# LESSON TWENTY ONE
## Starting Django

## description of folders and files
___FOLDERS__
1. __config__ - _base configuration files for django._
2. __core__ - _base configuration files for user project._
3. __migrations__ - _Project migration files._

__FILES__
1. __config/init.py__ - _An empty file that tells Python that this directory should be considered a Python package._
2. __config/asgi.py__ - _An entry-point for ASGI-compatible web servers to serve the project._
3. __config/settings.py__ - _Settings/configuration for Django project._
4. __config/urls.py__ - _The URL declarations for Django project; a “table of contents” of Django-powered site._
5. __config/wsgi.py__ - _An entry-point for WSGI-compatible web servers to serve the project._

1. __core/migrations/init.py__ - _An empty file that tells Python that this directory should be considered a Python package._

1. __core/init.py__ - _An empty file that tells Python that this directory should be considered a Python package._
2. __core/admin.py__ - _Used to display your models in the admin panel_
3. __core/apps.py__ - _Django contains a registry of installed applications that store configuration and provides introspection. It also maintains a list of available models._
4. __core/models.py__ - _A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table._
5. __core/tests.py__ - _A conventional place for tests  an application’s. You can write your own tests here._
6. __core/views.py__ - _This is where we will place the "logic" of our application._

1. __db.sqlite3__ - _Database file._
2. __manage.py__ - _A command-line utility that lets you interact with Django project in various ways._
3. __Pipfile__ - _Virtual environment requirements._
4. __Pipfile.lock__ - _The lock file is created on the basis of the Pipfile file itself._
5 __README.md__ - _Project description._