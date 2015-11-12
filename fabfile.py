__author__ = 'alexolivas'

from fabric.api import local, hosts
from fabric.colors import green


@hosts('localhost')
def deploy_development():
    print(green("starting the development server"))
    local('export APP_SETTINGS=djangorest.settings.development')
    # local('python manage.py makemigrations')
    # local('python manage.py migrate')
    local('python manage.py runserver')


@hosts('crinoid-stage.starfishsolutions.com')
def deploy_stage():
    print(green("deploying stage"))
    # local('svn update')
    local('export APP_SETTINGS=djangorest.settings.stage')
    # local('python manage.py makemigrations')
    # local('python manage.py migrate')
    # TODO: Command to restart the web server


@hosts('crinoid.starfishsolutions.com')
def deploy_production():
    print(green("deploying production"))
    # local('svn update')
    local('export APP_SETTINGS=djangorest.settings.production')
    # local('python manage.py makemigrations')
    # local('python manage.py migrate')
    # TODO: Command to restart the web server
