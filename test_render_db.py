import os
import django

# Test what happens when DATABASE_URL is set (like on Render)
os.environ['DATABASE_URL'] = 'postgresql://test:test@example.com/test'

# Configure Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings')
django.setup()

from django.conf import settings
print("Database engine:", settings.DATABASES['default']['ENGINE'])
print("Database name:", settings.DATABASES['default'].get('NAME', 'N/A'))
print("Database host:", settings.DATABASES['default'].get('HOST', 'N/A'))
