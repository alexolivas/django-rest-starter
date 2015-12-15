from fabric.api import local, hosts, task
from fabric.operations import run, env
from fabric.colors import green


@task
def clean_build_dev():
    print(green("running a clean development build.."))
    local('gulp clean-dev')
    local('gulp build-dev')


@task
def clean_watch_dev():
    print(green("watching a development build of the website.."))
    local('gulp clean-dev')
    local('gulp watch-dev')


@task
def test_deploy_dev_build():
    print(green("starting the server with a clean development build.."))
    local('gulp clean-dev')
    local('gulp build-dev')
    local('export APP_SETTINGS=djangorest.settings.development')
    local('python manage.py runserver')


@task
def backup_database():
    print(green("backing up the database.."))
    local('rm -r resources/db/refresh.json')
    local('./manage.py dumpdata > resources/db/refresh.json')


@task
def refresh_database():
    print(green("restoring the database from the last backup.."))
    local('./manage.py loaddata resources/db/refresh.json')


@task
def clean_build_prod():
    print(green("running a clean production build.."))
    local('gulp clean-prod')
    local('gulp build-prod')


@task
def clean_watch_prod():
    print(green("watching a production build of the website.."))
    local('gulp clean-prod')
    local('gulp watch-prod')


@task
def test_deploy_prod_build():
    # Used to test a production build before it is pushed out to a live production environment
    print(green("starting the local server with a clean production build.."))
    local('gulp clean-prod')
    local('gulp build-prod')
    # local('export APP_SETTINGS=djangorest.settings.production')
    local('python manage.py runserver --settings=django_website_skeleton.settings.production')


@hosts('sandbox1.webfactional.com')
@task
def stop_production_server():
    # TODO: Stop the server
    env.user = 'sandbox1'
    print(green("stopping the application server.."))


@hosts('sandbox1.webfactional.com')
@task
def start_production_server():
    # TODO: Stop the server
    env.user = 'sandbox1'
    print(green("starting the application server.."))


@hosts('sandbox1.webfactional.com')
@task
def run_production_build():
    # Follow https://www.caktusgroup.com/blog/2010/04/22/basic-django-deployment-with-virtualenv-fabric-pip-and-rsync/

    # TODO: Pull the latest from git
    # TODO: Install requirements.txt dependencies
    # TODO: Make migrations
    # TODO: migrate
    # TODO: Run a clean build > reference "fab clean_build_prod"

    env.user = 'sandbox1'
    print(green("starting the local server with a clean production build.."))
    run('cd webapps')
    run('ls')


@hosts('sandbox1.webfactional.com')
@task
def deploy():
    env.user = 'sandbox1'
    # TODO: Stop the server
    # run_production_build()
    # TODO: Move the contents of "static_prod" to "~/webapps/<django_static>"
    # TODO: set production settings: local('export APP_SETTINGS=djangorest.settings.production')
    # TODO: Restart the server
    print(green("starting the local server with a clean production build.."))
    run('cd webapps')