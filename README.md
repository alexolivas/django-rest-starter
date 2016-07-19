# Skeleton for Django REST Web Services
This is a barebones [django REST](http://www.django-rest-framework.org) web service project. The idea behind this project was to learn about django REST. The learning process gave birth to this skeleton project which can be used as a [starting point](#starting-a-new-project) for your own django REST project.
It comes pre-configured with several python library dependencies that I typically use in a django project, such as fabric, dj-database-url, whitenoise, and gunicorn. The project only contains user authentication and user profile endpoints. In other words, a user can only login, logout and view their profile info.
This makes the project useful for anyone wanting to start out with a basic token authentication system.

Visit the [api docs](http://django-rest-skeleton.herokuapp.com/docs) and login with the credentials user@email.com/secret to interact with the APIs or visit the [angular demo](http://angular-skeleton-11.herokuapp.com/) to interact with it an a real-world scenario.

[![wercker status](https://app.wercker.com/status/d873eeb709dfd4ad6b48edebe3823336/s/master "wercker status")](https://app.wercker.com/project/bykey/d873eeb709dfd4ad6b48edebe3823336)
[![Dependency Status](https://gemnasium.com/alexolivas/django-rest-skeleton.svg)](https://gemnasium.com/alexolivas/django-rest-skeleton)


## Table of Contents

- [Pre Requisites](#pre-requisites)
- [Getting Started](#getting-started)
- [Starting New Project](#starting-a-new-project)
- [Fab Tasks](#fab-tasks)
- [Wercker/Heroku Deployment](#wercker-and-heroku-deployment)

-------
# Pre Requisites
Before getting started with this django project its recommended that you create a virtual environment and setup your development database.

## Virtual Environments
It is recommended that you create a virtual environment to install the project's dependencies without having to worry about clashing dependencies with other python projects.

If you haven't installed virtualenv do so via pip
```bash
pip install virtualenv
```

Install virtualenvwrapper
```bash
pip install virtualenvwrapper
```

Create a directory to store details of your future virtual environments (this can be whatever location you'd like but remember it for the next step).
```bash
cd ~
mkdir .virtualenvs
mkdir Development/
```

Edit the bash profile (create it if it doesn't exist)
```bash
vi ~/.bash_profile
```

Add the following to your bash_profile
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Development
source /usr/local/bin/virtualenvwrapper.sh
```

Run the following command, if installed correctly, you will get a help menu
```bash
mkvirtualenv
```

Last step to be able to work with virtualenvwrapper and environment variables.
```bash
vi ~/.virtualenvs/postactivate
```

Add the following code snippet inside postactivate so that the project's environment variables are available on activate
```
set -a
. .env
set +a
```

## Database Setup
During the development phase I typically use a postgres database to simulate production as much as possible. These are the database setup instructions I use for my django and django-rest projects.

Install postgres if it is not already in your system
```bash
brew install postgresql
```

PSQL into postgres
```bash
psql postgres
```

Create users and database instances
```psql
postgres=# CREATE USER postgres WITH SUPERUSER;
CREATE DATABASE <database-name>;
GRANT ALL PRIVILEGES ON DATABASE <database-name> TO postgres;
CREATE USER <db-user> WITH PASSWORD '<password>';
GRANT ALL PRIVILEGES ON DATABASE <database-name> TO <db-user>;
```

# Getting Started
The first step to start working on this project is to [fork](https://github.com/alexolivas/django-rest-skeleton/edit/master/README.md#fork-destination-box) this repository into your github account. Then clone it into your local development environment:
```bash
git clone https://github.com/<your-account-or-organization>/django-rest-skeleton.git
```

Create an environment variables file
```bash
vi .env
```

Populate it with the following (generate the SECRET_KEY with a tool like 1password: 50 characters)
```
SECRET_KEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
DEBUG=True
DATABASE_URL='postgres://<db-user>@localhost:5432/<db_name>'
```

Create a new virtual wrapper environment
```bash
mkvirtualenv django-rest-skeleton
```

Install the project's requirements
```bash
pip install -r requirements.txt
```

Run the fab task to initialize your environment with a clean database (creates admin user with credentials admin/admin)
```bash
fab dev
```

Create a super user so that you can login to the admin site
```bash
 python manage.py createsuperuser
 ```

# Starting a New Project
If you want to clone this project and use it as a starting point for a new project first:

Clone the project with a different name
```bash
git clone https://github.com/alexolivas/django-rest-skeleton.git <project-name>
```

Remove the origin so that you can add your own repository as the new origin
```bash
cd <project-name>
git remote rm origin
git remote add origin <your-projects-git-repo>
git push -u origin master
```

Create an environment variables file
```bash
vi .env
```

Populate it with the following (generate the SECRET_KEY with a tool like 1password: 50 characters)
```
SECRET_KEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
DEBUG=True
DATABASE_URL='postgres://<db-user>@localhost:5432/<db_name>'
```

Rename the project (can be different than the project directory name)
```bash
mv django_website_skeleton/ <project-name>
```

Create a new virtual wrapper environment
```bash
mkvirtualenv <project-name>
```

Delete the database refresh json file (contains data that pertains to the django-website-skeleton project)
```bash
rm -rf <project-name>/resources/db/refresh.json
```

Replace the original project's name with your project (same name as in step 3) in manage.py
```bash
perl -pi -e 's/django_website_skeleton/<project-name>/g' manage.py 
```

Do the exact same thing (same name as in step 3) to the wsgi.py file
```bash
perl -pi -e 's/django_website_skeleton/<project-name>/g' <project-name>/wsgi.py
```

Do a final search/replace of django_website_skeleton to replace with your project's name using your IDE's search/replace feature.

Commit your project's name changes
```bash
git commit -a -m "Renamed Project"
```

Install the project's requirements
```bash
pip install -r requirements.txt
```

Run the following tasks to initialize your new project's environment
```bash
fab migrate_db
```

# Fab Tasks
Start a local web server, using gunicorn (http://0.0.0.0:5000). Use this task to test the system running in a gunicorn (heroku-like) environment
```bash
fab start_gunicorn
```

Starts the Django development server ((http://localhost:8000), a lightweight Web server written purely in Python
```bash
fab start_webserver
```

Install the project's requirements
```bash
fab install_requirements
```

Apply database migrations
```bash
fab migrate_db
```

Restore the database to a clean state
```bash
fab refresh_database
```

Create a backup of the database in it's current state
```bash
fab backup_database
```

Generate a new dev static resources build
```bash
fab clean_build_dev
```

Run python tests
```bash
fab test
```

# Wercker And Heroku Deployment
This project's demo is continuously built by [wercker](http://wercker.com/) and deployed by the push of a button to [heroku](http://heroku.com). I followed the [wercker deployments steps](http://devcenter.wercker.com/quickstarts/deployment/heroku.html) to get the app deployed.
