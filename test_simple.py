import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings')
django.setup()

from django.conf import settings
print(f"✅ Django settings loaded successfully!")
print(f"Database: {settings.DATABASES['default']['ENGINE']}")
print(f"Debug mode: {settings.DEBUG}")
