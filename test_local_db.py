import os
import django

# Test without DATABASE_URL (local development)
if 'DATABASE_URL' in os.environ:
    del os.environ['DATABASE_URL']

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings')
django.setup()

from django.conf import settings
print("Local Database engine:", settings.DATABASES['default']['ENGINE'])
print("Local Database name:", settings.DATABASES['default'].get('NAME', 'N/A'))
