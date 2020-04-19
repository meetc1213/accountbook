from jpisclubs.common import *
SECRET_KEY = config('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['jpisclubs.herokuapp.com']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATIC_ROOT=os.path.join(BASE_DIR,'static')
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
import dj_database_url
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)