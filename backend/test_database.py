import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings_production')
django.setup()

from django.db import connection

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Database connected successfully!")
        print(f"PostgreSQL version: {version[0]}")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
