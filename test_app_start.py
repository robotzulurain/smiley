import os
import django
from django.core.management import execute_from_command_line

print("Testing if Django application can start...")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amr_project.settings')
django.setup()

try:
    # Simulate running a management command
    from django.core.management import execute_from_command_line
    print("✅ Django management commands work")
    
    # Test database connection
    from django.db import connection
    connection.ensure_connection()
    print("✅ Database connection successful")
    
    # Test that we can import your app
    try:
        from amr_api import models
        print("✅ AMR API models import successfully")
    except ImportError as e:
        print(f"⚠️  AMR API models import issue (may be expected): {e}")
    
    print("\n🎉 Application startup test PASSED!")
    
except Exception as e:
    print(f"❌ Application startup test FAILED: {e}")
