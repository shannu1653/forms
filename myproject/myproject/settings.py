from pathlib import Path
import os
from dotenv import load_dotenv
import pymysql

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# SECURITY
# -----------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "your-default-secret-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
# optional: add your Render URL directly for testing
ALLOWED_HOSTS.append("forms-2-2ajg.onrender.com")

# -----------------------------
# INSTALLED APPS
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'form',  # your app
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # must be after SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -----------------------------
# URLS & WSGI
# -----------------------------
ROOT_URLCONF = 'myproject.urls'
WSGI_APPLICATION = 'myproject.wsgi.application'

# -----------------------------
# TEMPLATES
# -----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'form/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -----------------------------
# DATABASE (MySQL + optional SSL for Render)
# -----------------------------
pymysql.install_as_MySQLdb()

ssl_ca_path = "/etc/secrets/mysql-ca.pem"
ssl_options = {}
if os.path.exists(ssl_ca_path):
    ssl_options = {'ssl': {'ca': ssl_ca_path}}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DB'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': os.environ.get('MYSQL_HOST'),
        'PORT': os.environ.get('MYSQL_PORT', '3306'),
        'OPTIONS': ssl_options,
    }
}

# -----------------------------
# PASSWORD VALIDATION
# -----------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------
# INTERNATIONALIZATION
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------
# STATIC FILES (WhiteNoise / Render)
# -----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -----------------------------
# DEFAULT PRIMARY KEY
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# -----------------------------
# SECURITY
# -----------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "your-default-secret-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "False") == "True"

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
ALLOWED_HOSTS.append("forms-2-2ajg.onrender.com")  # optional: your Render URL

# CSRF trusted origins (fixes 403 CSRF error)
CSRF_TRUSTED_ORIGINS = [
'https://forms-d3jh.onrender.com',
]

# Optional: secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
