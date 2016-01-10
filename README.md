# Skeleton for Django REST Web Services
This project serves as a starting point to build a [Django REST](http://www.django-rest-framework.org) web service. This project ships with token based authentication but can be modified to use any other [authentication schemes](http://www.django-rest-framework.org/api-guide/authentication/).

## Table of Contents

- [Pre Requisites](#pre-requisites)
- [Getting Started](#getting-started)
- [Starting New Project](#starting-a-new-project)
- [Notes](#notes)

-------
# Pre Requisites
It is recommended that you create a virtual environment to install the project's dependencies without having to worry about clashing dependencies with other python projects.
* If you haven't installed virtualenv do so via pip
```bash
pip install virtualenv
```

* Install virtualenvwrapper
```bash
pip install virtualenvwrapper
```

* Create a directory to store details of your future virtual environments (this can be whatever location you'd like but remember it for the next step).
```bash
cd ~
mkdir .virtualenvs
mkdir Development/
```

* Edit the bash profile (create it if it doesn't exist)
```bash
vi ~/.bash_profile
```

Add the following to your bash_profile
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Development/
source /usr/local/bin/virtualenvwrapper.sh
```

* Run the following command to verify that the virtual environment wrapper was successfully installed, it should spit out the options related to it
```bash
mkvirtualenv
```

# Getting Started
* To get this project running locally on your computer, first clone it
```bash
git clone https://github.com/alexolivas/django-rest-skeleton.git
```

* Create a new virtual wrapper environment
```bash
mkvirtualenv django-rest-skeleton
```

* Install the requirements
```bash
pip install -r requirements.txt
```

* Run the initial database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

* Refresh the database
```bash
fab refresh_database
fab test_deploy_dev_build
```

# Starting a New Project
If you want to clone this project and use it as a starting point for a new project first:

* Clone the project with a different name
```bash
git clone https://github.com/alexolivas/django-rest-skeleton.git <project-name>
```

* Remove the origin so that we can later set another GIT repository as the new origin 
```bash
cd <project-name>
git remote rm origin
```

* Rename the project (can be different than the project directory name)
```bash
mv djangorest/ <project-name>
```

* Update the origin to your new git repository and push the changes
```bash
git remote add origin <your-projects-git-repo>
git push -u origin master
```

* Create a new virtual wrapper environment
```bash
mkvirtualenv <project-name>
```

* Install the requirements
```bash
pip install -r requirements.txt
```

* Replace the original project's name with your project (same name as in step 3) in manage.py
```bash
perl -pi -e 's/djangorest/<project-name>/g' manage.py 
```

* Do the exact same thing (same name as in step 3) to the wsgi.py file
```bash
perl -pi -e 's/djangorest/<project-name>/g' <project-name>/wsgi.py
```

* One last search and replace: now in the base settings file
```bash
perl -pi -e 's/djangorest/<project-name>/g' <project-name>/settings/base.py
```

* Commit your project name changes
```bash
git commit -a -m "Renamed Project"
```

* Run the initial database migrations
```bash
python manage.py migrate
```

* Create an admin user (optional)
```bash
python manage.py syncdb
```

* Finally, generate a new secret key (using a tool like 1password) and update settings/development.py with it 
and commit your changes. You now have a running bare bones DjangoRest project with token authentication. Build away.
