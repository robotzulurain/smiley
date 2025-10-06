#!/bin/bash
# Try to run from current directory, fall back to backend directory
if [ -f "manage.py" ]; then
    python manage.py migrate
    python manage.py createsuperuser --noinput --username admin --email robotzulurain@gmail.com 2>/dev/null || true
    gunicorn amr_project.wsgi:application --bind 0.0.0.0:$PORT
elif [ -f "backend/manage.py" ]; then
    cd backend
    python manage.py migrate
    python manage.py createsuperuser --noinput --username admin --email robotzulurain@gmail.com 2>/dev/null || true
    gunicorn amr_project.wsgi:application --bind 0.0.0.0:$PORT
else
    echo "Error: manage.py not found in current directory or backend/"
    exit 1
fi
