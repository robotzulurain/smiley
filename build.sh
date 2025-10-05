#!/bin/bash
pip install -r requirements.txt
python manage.py collectstatic --noinput
chmod +x startup.sh
