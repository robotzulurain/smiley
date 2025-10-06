import os
import sys

print("=== Deployment Verification ===")

# Check critical environment variables
required_vars = [
    'DATABASE_URL',
    'SECRET_KEY', 
    'DEBUG',
    'ALLOWED_HOSTS',
    'DJANGO_SETTINGS_MODULE'
]

all_good = True
for var in required_vars:
    if var in os.environ:
        value = os.environ[var]
        if var == 'DATABASE_URL' and '@' in value:
            # Mask password in DATABASE_URL
            parts = value.split('@')
            user_pass = parts[0]
            if ':' in user_pass:
                user, _ = user_pass.split(':', 1)
                masked = f"{user}:****@{parts[1]}"
                print(f"✅ {var}: {masked}")
            else:
                print(f"✅ {var}: [set]")
        else:
            print(f"✅ {var}: {value}")
    else:
        print(f"❌ {var}: NOT SET")
        all_good = False

print(f"\nStatus: {'✅ All environment variables are set' if all_good else '❌ Missing environment variables'}")
