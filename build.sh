#!/usr/bin/env bash
set -o errexit

echo "=== Starting Build Process ==="

# Navigate to backend directory
cd backend

echo "=== Upgrading pip ==="
pip install --upgrade pip

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Collecting static files ==="
python manage.py collectstatic --noinput

echo "=== Build completed successfully ==="
