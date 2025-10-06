import os

print("=== Environment Variables ===")
print(f"DATABASE_URL: {'SET' if 'DATABASE_URL' in os.environ else 'NOT SET'}")
print(f"SECRET_KEY: {'SET' if 'SECRET_KEY' in os.environ else 'NOT SET'}")
print(f"DEBUG: {os.environ.get('DEBUG', 'NOT SET')}")
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE', 'NOT SET')}")

# Mask database URL for security
if 'DATABASE_URL' in os.environ:
    db_url = os.environ['DATABASE_URL']
    if '@' in db_url:
        parts = db_url.split('@')
        user_pass = parts[0]
        if ':' in user_pass:
            user, password = user_pass.split(':', 1)
            masked = f"{user}:****@{parts[1]}"
            print(f"DATABASE_URL (masked): {masked}")
