import os
import sys

print("=== Verifying Django App Structure ===")

apps = ['amr_api', 'amr_reports']
base_dir = os.path.dirname(os.path.abspath(__file__))

all_good = True
for app in apps:
    app_path = os.path.join(base_dir, app)
    required_files = ['__init__.py', 'apps.py', 'models.py']
    
    if os.path.exists(app_path):
        print(f"✅ {app} directory exists")
        for file in required_files:
            file_path = os.path.join(app_path, file)
            if os.path.exists(file_path):
                print(f"  ✅ {file} exists")
            else:
                print(f"  ❌ {file} missing")
                all_good = False
    else:
        print(f"❌ {app} directory missing")
        all_good = False

if all_good:
    print("🎉 All app structure checks passed!")
else:
    print("❌ Some app structure issues found")
    sys.exit(1)
