#!/bin/bash
python manage.py migrate
python manage.py createsuperuser --noinput --username admin --email robotzulurain@gmail.com --password AmrAdmin2024! 2>/dev/null || true
gunicorn amr_project.wsgi:application --bind 0.0.0.0:$PORT
