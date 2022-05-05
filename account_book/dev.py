from account_book.common import *
SECRET_KEY = '@(g2e0_lg1i@3y1&u57hw)bzr#vnh1!-_j5x-vr7)%+o*%^c)%'
DEBUG=True
ALLOWED_HOSTS = ['*']
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