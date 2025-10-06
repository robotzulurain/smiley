#!/bin/bash
# Run from root directory since manage.py is here
python manage.py migrate
python manage.py createsuperuser --noinput --username admin --email robotzulurain@gmail.com 2>/dev/null || true
gunicorn amr_project.wsgi:application --bind 0.0.0.0:$PORT
