import os
import django
from django.db import connection

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings_production')
django.setup()

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        print("✅ Database connection successful!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
