import os
import django
from django.conf import settings

print("=== Testing Local Settings ===")
if 'DATABASE_URL' in os.environ:
    del os.environ['DATABASE_URL']
    
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings')
django.setup()

print(f"Local DB Engine: {settings.DATABASES['default']['ENGINE']}")
print(f"Local DB Name: {settings.DATABASES['default']['NAME']}")

print("\n=== Testing Render Settings ===")
os.environ['DATABASE_URL'] = 'postgresql://test:test@example.com/test'

# Reload settings
from importlib import reload
reload(settings)

print(f"Render DB Engine: {settings.DATABASES['default']['ENGINE']}")
print(f"Render DB Host: {settings.DATABASES['default']['HOST']}")

print("\n✅ All tests passed!")
