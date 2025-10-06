#!/usr/bin/env bash
set -o errexit

echo "=== Starting Build Process ==="
echo "Current directory: $(pwd)"
echo "Contents:"
ls -la

echo "=== Navigating to backend ==="
cd backend
echo "Now in: $(pwd)"
echo "Backend contents:"
ls -la

echo "=== Upgrading pip ==="
pip install --upgrade pip

echo "=== Installing dependencies ==="
pip install -r requirements.txt

echo "=== Collecting static files ==="
python manage.py collectstatic --noinput

echo "=== Build completed successfully ==="
