# django-rest-skeleton

## Getting Started
* Clone the project
```bash
git clone https://github.com/alexolivas/django-rest-skeleton.git <project-name>
```

* Remove the origin so that we can later set another GIT repository as the new origin 
```bash
cd <project-name>
git remote rm origin
```

* Update the origin to your new git repository
```bash
git remote add origin <your-projects-git-repo>
```

* Initial Commit to your repository
```bash
git add .
git commit -m "Initial Commit"
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
and commit your changes. You now have a running bare bones Django project. Build away.

## Notes
To create apps inside the apps directory:
```bash
mkdir apps/home
python manage.py startapp home apps/home
```
