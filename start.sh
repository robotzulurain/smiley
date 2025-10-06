#!/usr/bin/env bash
set -o errexit

echo "=== Starting AMR Backend ==="

# Navigate to backend directory
cd backend

echo "=== Applying database migrations ==="
python manage.py migrate

echo "=== Creating superuser ==="
python create_superuser.py || echo "Superuser creation completed"

echo "=== Starting Gunicorn ==="
exec gunicorn amr_project.wsgi:application --bind 0.0.0.0:$PORT --access-logfile -
