import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings_production')
os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_jZXHKdP8UL5f@ep-little-pine-ada2gu0j-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require'

django.setup()

from django.db import connection

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Database connected successfully!")
        print(f"PostgreSQL version: {version[0]}")
        
        # Test if we can create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_connection (
                id SERIAL PRIMARY KEY,
                test_text TEXT,
                created_at TIMESTAMP DEFAULT NOW()
            )
        """)
        print("✅ Table creation test passed!")
        
except Exception as e:
    print(f"❌ Database connection failed: {e}")
