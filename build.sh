#!/bin/bash
pip install --upgrade pip
pip install -r requirements.txt

# Check if we're in the right directory and try backend if needed
if [ -f "manage.py" ]; then
    python manage.py collectstatic --noinput
elif [ -f "backend/manage.py" ]; then
    cd backend && python manage.py collectstatic --noinput
else
    echo "Error: manage.py not found in current directory or backend/"
    exit 1
fi
