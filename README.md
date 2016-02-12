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
- [Wercker/Heroku Support](#wercker-and-heroku-support)

-------
# Pre Requisites
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
export PROJECT_HOME=$HOME/Development/
source /usr/local/bin/virtualenvwrapper.sh
```

Run the following command to verify that the virtual environment wrapper was successfully installed, it should spit out the options related to it
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

# Getting Started
To get this project running locally on your computer, first clone it
```bash
git clone https://github.com/alexolivas/django-rest-skeleton.git
```

Create an environment variables file
```bash
vi .env
```

Populate it with the following (generate the SECRET_KEY with a tool like 1password: 50 characters)
```
SECRET_KEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
DEBUG=True
DATABASE_URL='postgres://postgres@localhost:5432/<db_name>'
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
DATABASE_URL='postgres://postgres@localhost:5432/<db_name>'
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

Install the project's requirements
```bash
fab install_requirements
```

Apply database migrations
```bash
fab migrate_db
```

Collect static files using django's collectstatic command
```bash
fab collect_static
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

Start a node server watching for changes to static assets
```bash
fab watch_dev
```

Run python tests
```bash
fab test
```

# Wercker And Heroku Support
[Wercker](http://devcenter.wercker.com/index.html) is a build automation tool that can be used to build and deploy your apps in containers.
[Heroku](https://www.heroku.com) is a cloud Platform-as-a-Service supporting several programming languages. 

## Wercker
* Login to wercker website
* Navigate to your project's settings
* Create a new deploy target
* Add the following environment variables (inside the target) > HEROKU_USER, HEROKU_APP_NAME, HEROKU_KEY, HEROKU_KEY_PAIR
* The heroku_key_pair should be generate in SSH_KEYS. [Click here](http://devcenter.wercker.com/quickstarts/deployment/heroku.html) for a complete step-by-step tutorial.

## Heroku
* Login to the heroku website.
* Copy the public key you generated in wercker and add it to heroku (manage account > SSH Keys)
* Go into the project > settings > add the following config variables > DATABASE_URL, DEBUG (don't add this if production), SECRET_KEY
* Open up your terminal and login
```bash
heroku login
```

Set the heroku repo as a remote
```bash
heroku git:remote -a <heroku-project-name>
OR
git remote add <custom-name> https://git.heroku.com/<heroku-project-name>.git
```

Add nodejs and python buildpacks so heroku knows what to build
```bash
heroku buildpacks:add heroku/python
heroku buildpacks:add --index 1 heroku/nodejs
```

Run a test production deployment on your local environment to simulate the system running with production settings in a gunicorn (heroku-like) environment 
```bash
pip install -r requirements.txt
fab test_prod_deploy
fab start_gunicorn
```

To deploy using heroku CLI instead of wercker use
```bash
git push heroku master
```

For complete documentation on heroku + django go to https://devcenter.heroku.com/articles/django-app-configuration.
