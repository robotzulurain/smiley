"""
Local development settings for AMR Surveillance Application
"""
from .settings_production import *

# Override for local development
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Use SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Disable some security settings for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
