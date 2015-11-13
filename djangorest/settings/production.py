from base import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# TODO: Generate a new key in the file system and place in the directory
SECRET_KEY = open(os.path.expanduser('~/.gallery-secret')).read().strip()
# SECRET_KEY = '88uh$_ln*xk$7ej1x!(9fy2q99ct1s$9p-sbz40b@1ad-o=9@)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# TODO: Add URLS that are allowed to call this Service
ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# TODO: Do not add your DB password here and commit to version control, keep it secret on the production server
# TODO: just like the key
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
