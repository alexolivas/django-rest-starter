from fabric.api import local, hosts, task
from fabric.colors import green


@task
def dev():
    print(green("******** initializing a clean development environment ********"))
    collect_static()
    migrate_db()
    refresh_database()


@task
def deploy():
    print(green("******** initializing production environment deployment test ********"))
    test()
    migrate_db()


@task
def install_requirements():
    print(green("installing project requirements.."))
    local('pip install -r requirements.txt')


@task
def upgrade_pip():
    local('pip install --upgrade pip')


@task
def migrate_db():
    print(green("applying database migrations.."))
    local('python manage.py makemigrations')
    local('python manage.py migrate')


@task
def refresh_database():
    print(green("restoring the database from the last backup.."))
    local('./manage.py loaddata django_website_skeleton/resources/db/refresh.json')


@task
def collect_static():
    print(green("collecting static files.."))
    local('python manage.py collectstatic --noinput')


@task
def backup_database():
    print(green("backing up the database.."))
    local('rm -r django_website_skeleton/resources/db/refresh.json')
    local('./manage.py dumpdata > django_website_skeleton/resources/db/refresh.json')


@task
def start_gunicorn():
    print(green("starting the gunicorn server with a clean development build.."))
    local('foreman start')


@task
def start_webserver():
    print(green("starting the django web server with a clean development build.."))
    local('python manage.py runserver')


@task
def test():
    local('python manage.py test')
