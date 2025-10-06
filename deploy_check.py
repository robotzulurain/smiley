import os
import sys

print("🚀 FINAL DEPLOYMENT CHECKLIST 🚀")
print("=" * 50)

# Check critical files
files_to_check = {
    'requirements.txt': 'Dependencies',
    'runtime.txt': 'Python version', 
    'render.yaml': 'Render configuration',
    'amr_project/settings.py': 'Django settings',
    'manage.py': 'Django management'
}

all_good = True
for file, description in files_to_check.items():
    if os.path.exists(file):
        print(f"✅ {description:20} {file}")
    else:
        print(f"❌ {description:20} {file} - MISSING!")
        all_good = False

# Check settings configuration
print("\n📋 Settings Configuration:")
try:
    with open('amr_project/settings.py', 'r') as f:
        content = f.read()
    
    checks = [
        ('import dj_database_url', 'Database URL import'),
        ("if 'DATABASE_URL' in os.environ", 'Render detection'),
        ('dj_database_url.config', 'Database config'),
        ('DEBUG = True', 'Debug mode (should be False in production)')
    ]
    
    for check, description in checks:
        if check in content:
            status = "✅" 
        else:
            status = "⚠️" if check != 'DEBUG = True' else "❌"
        print(f"   {status} {description}")
        
except Exception as e:
    print(f"   ❌ Could not read settings: {e}")
    all_good = False

# Check requirements
print("\n📦 Package Versions:")
try:
    import django
    print(f"   ✅ Django {django.__version__}")
except ImportError:
    print("   ❌ Django not installed")

try:
    import dj_database_url
    print("   ✅ dj-database-url installed")
except ImportError:
    print("   ❌ dj-database-url not installed")

try:
    import psycopg2
    print("   ✅ psycopg2-binary installed")
except ImportError:
    print("   ❌ psycopg2-binary not installed")

if all_good:
    print("\n🎉 DEPLOYMENT READY!")
    print("Next steps:")
    print("1. git add . && git commit -m 'Ready for deployment'")
    print("2. git push origin main") 
    print("3. Go to render.com and create new Web Service")
    print("4. Connect your GitHub repository")
    print("5. Add DATABASE_URL environment variable")
    print("6. Deploy!")
else:
    print("\n❌ Some issues need to be fixed before deployment.")
