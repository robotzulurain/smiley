#!/bin/bash
python manage.py collectstatic --noinput
python manage.py migrate
gunicorn amr_project.wsgi:application --bind 0.0.0.0:$PORT
