import os

print("=== Environment Variables ===")
print(f"DATABASE_URL: {'SET' if 'DATABASE_URL' in os.environ else 'NOT SET'}")
print(f"SECRET_KEY: {'SET' if 'SECRET_KEY' in os.environ else 'NOT SET'}")
print(f"DEBUG: {os.environ.get('DEBUG', 'NOT SET')}")
print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE', 'NOT SET')}")

# Show more details about DATABASE_URL
if 'DATABASE_URL' in os.environ:
    db_url = os.environ['DATABASE_URL']
    print(f"\n=== DATABASE_URL Details ===")
    
    # Extract host information
    if '@' in db_url:
        host_part = db_url.split('@')[1].split('/')[0]
        print(f"Database Host: {host_part}")
        
        # Check if it has the correct c-2 subdomain
        if 'c-2' in host_part:
            print("✅ Database host contains correct 'c-2' subdomain")
        else:
            print("❌ Database host is MISSING 'c-2' subdomain!")
    
    # Mask password for security
    if '@' in db_url:
        parts = db_url.split('@')
        user_pass = parts[0]
        if ':' in user_pass:
            user, password = user_pass.split(':', 1)
            masked = f"{user}:****@{parts[1]}"
            print(f"DATABASE_URL (masked): {masked}")
