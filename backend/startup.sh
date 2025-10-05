#!/usr/bin/env bash
# Exit on error
set -o errexit

# Apply database migrations
python manage.py migrate

# Create superuser if it doesn't exist
python manage.py create_superuser.py || true

# Start Gunicorn
exec gunicorn amr_project.wsgi:application --bind 0.0.0.0:$PORT
