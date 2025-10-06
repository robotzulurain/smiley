#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "=== Starting AMR Backend ==="
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "DJANGO_SETTINGS_MODULE: $DJANGO_SETTINGS_MODULE"

# Check environment
python check_env.py

# Apply database migrations
echo "=== Applying database migrations ==="
python manage.py migrate

# Create superuser if it doesn't exist
echo "=== Creating superuser ==="
python create_superuser.py || echo "Superuser creation completed"

# Start Gunicorn
echo "=== Starting Gunicorn ==="
exec gunicorn amr_project.wsgi:application --bind 0.0.0.0:$PORT --access-logfile -
